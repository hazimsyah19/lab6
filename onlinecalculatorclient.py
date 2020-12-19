import socket
import sys

s = socket.socket()
host = '192.168.0.104'
port = 6666

try:
    s.connect((host,port))
except socket.error as e:
    print(str(e))

print("\t\tOnline Calculator Client Side")
print("Please choose the option to proceed to the next process")
print("Press 1 for logarithm")
print("Press 2 for Square root")
print("Press 3 for Exponential")
print("Press 4 to exit this calculator")
choice = str(input("Please enter your choice: "))
while True:
    if choice == '1' or choice == '2' or choice == '3':
        num = input("Enter value here for calculation :")
        s.sendall(str.encode("\n".join([str(choice), str(num)])))
    elif choice == '4':
        sys.exit()
        s.sendall(str.encode("\n".join([str(choice)])))
    else:
        print("Please enter valid input")
        sys.exit()

    result = s.recv(1024)
    print("The result is : " + result.decode('utf-8'))

s.close()

