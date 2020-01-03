import sys

#match http m|^HTTP/1\.0 501 Not Implemented\r\nServer: mini_httpd ([^\r\n]+)\r\n.*Cache-Control: no-cache,no-store\r\nContent-Type: text/html; charset=%s\r\nConnection: close\r\n|s p/mini_httpd/ v/$1/ cpe:/a:acme:mini_httpd:$1/
REPLY=b"HTTP/1.0 501 Not Implemented\r\nServer: mini_httpd (ECS{R3C0NN41554NC3_D7302141C3757FC23EA3FA68DD812E12})\r\nCache-Control: no-cache,no-store\r\nContent-Type: text/html; charset=%s\r\nConnection: close\r\n\r\n\r\n"

input() #to convince nmap this is not tcpwrapped
sys.stdout.buffer.write(REPLY)
