import socket

ClientSocket = socket.socket()
host = '192.168.0.104'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host,port))
except socket.error as e:
    print(str(e))

response = ClientSocket.recv(1024)
print(response)
while True:
    Input = input("Say something : ")
    ClientSocket.send(str.encode(Input))
    response = ClientSocket.recv(1024)
    print(response.decode('utf-8'))

ClientSocket.close()
