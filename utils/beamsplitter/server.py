import os
import socket
import stat
import struct
import logging
import secrets
import datetime
from time import sleep
from docker import from_env as docker_init

validservices=["lfi","sqli","bsqli"]
services={}
MAX_SERVICES=50
ERROR="http://localhost:8080/webchal/error.html?"
EXPIRED="http://localhost:8080/webchal/expired.html?"
NAUGHTY="http://localhost:8080/webchal/naughty.html?"

def gencookie():
    return secrets.token_hex(32)

def init():
    global sock, docker
    logging.basicConfig(level=logging.DEBUG)
    sockaddr="/var/run/beamsplitter.sock"
    if os.path.exists(sockaddr):
        try:
            os.unlink(sockaddr)
        except:
            logging.critical("Another beamsplitter seems to be running!")
            exit(1)
    sock=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
    sock.bind(sockaddr)
    os.chmod(sockaddr, stat.S_IRWXU|stat.S_IRWXG) #0770
    os.chown(sockaddr,0,1011) #owned by root:beamsplitter,
    #so people in the beamsplitter group can connect
    sock.listen(1)
    docker=docker_init()

'''
def getpid(conn):
    credstruct=conn.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12)
    pid,uid,gid=struct.unpack("III",credstruct)
    logging.debug("PID=%d UID=%d GID=%d"%(pid,uid,gid))
    return pid

def processA():
    #docker.containers.run("debian", "echo hello world", remove=True, tty=True, user=1000, detach=True)
    pass
'''

class Service:
    def __init__(self,imgname,port):
        self.name=imgname
        self.port=port
        self.container=docker.containers.run(imgname, remove=True, detach=True, ports={'80/tcp':('127.0.0.1',port)})
        self.creationtime=datetime.datetime.now()
        self.lastaccesstime=datetime.datetime.now()
        self.alive=True
    def destroy(self):
        self.container.kill()
        self.alive=False
    def getaddr(self):
        if not self.alive:
            return EXPIRED
        self.lastaccesstime=datetime.datetime.now()
        return "http://localhost:%d"%self.port
    def __repr__(self):
        return "%s service %s running on port %d, created %s, last accessed %s"%("Alive" if self.alive else "Dead", self.name, self.port, self.creationtime, self.lastaccesstime)

def createInstance(name):
    global nextport
    nextport=40001
    while sum([1 for i in services.values() if i.alive and i.port==nextport])!=0 or nextport>40010+MAX_SERVICES:
        nextport+=1
    if(nextport>40010+MAX_SERVICES): #Way too many instances
        logging.critical("Way too many instances?????")
        logging.critical(services)
        return ""
    s=Service(name,nextport)
    nextport+=1
    cookie=gencookie()
    while cookie in services:
        cookie=gencookie()
    services[cookie]=s
    sleep(5)
    return "S%s"%cookie

def routinecleanup():
    curtime=datetime.datetime.now()
    for s in [i for i in services.values() if i.alive and (curtime-i.creationtime).days>1]:
        s.destroy()
    alive=[i for i in services.values() if i.alive]
    if len(alive)>MAX_SERVICES:
        alive.sort(key=lambda s:s.lastaccesstime)
        alive=alive[:-MAX_SERVICES]
        for s in alive:
            s.destroy()


def serve():
    while True:
        conn, _=sock.accept()
        try:
            #logging.debug("Connection received")
            data=conn.recv(1)
            if data==b"R":
                data=conn.recv(1000).decode()
                #logging.debug("Got a request: %s"%data)
                service=data.split('_')[0]
                if service not in validservices:
                    conn.sendall(NAUGHTY.encode())
                    continue
                cookies=data[len(service)+1:].split("; ")
                ins=None
                for s in cookies:
                    if s.startswith("beamsplitter_%s="%service):
                        token=s.split("=")[1]
                        if token in services:
                            ins=services[token]
                if ins:
                    conn.sendall(ins.getaddr().encode())
                else:
                    conn.sendall(ERROR.encode())
            elif data==b"C":
                data=conn.recv(1000).decode()
                if data not in validservices:
                    logging.warning("Asked to create nonexistent service %s!"%data)
                    conn.sendall(b"F")
                    continue
                logging.info("Asked to create instance of %s"%data)
                conn.sendall(createInstance(data).encode())
            elif data==b"D":
                #Debug mode
                logging.info("Dumping debug info")
                for c,s in services.items():
                    print(c)
                    print(s)
            else:
                logging.debug("Didn't receive anything, closing")
            routinecleanup()
        except Exception as e:
            logging.exception(e)
            continue
        finally:
            conn.close()

def cleanup():
    logging.info("Cleaning up...")
    sock.close()
    docker.close()
    for s in [i for i in services.values() if i.alive]:
        s.destroy()
    os.unlink("/var/run/beamsplitter.sock")


init()
try:
    serve()
finally:
    cleanup()
