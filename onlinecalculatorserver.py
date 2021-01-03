import socket
import sys
import math
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process(conn):
    conn.send(str.encode("Welcome to the server\n"))
    #print(num)
    while True:
        num = conn.recv(2048).decode('utf-8').split('\n')
        print(num)
        if num[0] == '1':
            ans = math.log(int(num[1]))
            print(ans)
        elif num[0] == '2':
            ans = math.sqrt(int(num[1]))
        elif num[0] == '3':
            ans = math.exp(int(num[1]))
        else:
            break

        conn.sendall(str.encode(str(ans)))
    conn.close()

if __name__ == '__main__':
    s = socket.socket()
    port = 6666
    s.bind(('',port))
    print("[*]:Listening...")
    s.listen(5)
    try:
        while True:
            try:
                conn,addr = s.accept()
                print("[*]:Got connection from " + addr[0] + ":" +str(addr[1]))  
                p = Process(target=process,args=(conn,))
                p.start()
            except socket.error:
                print("socket error")
    except Exception as e:
        print("An exception occured")
        print(e)
             

