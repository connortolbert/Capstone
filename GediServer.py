import socket
import time
import motors
import squaredemo as sqd

full_msg =''    #empty string to store data in
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 , TCP
s.bind(("192.168.1.3", 65530))  # host name/IP address, port
s.listen(5)  # set queue

while True:
    #if (int(full_msg) < 1):
        full_msg =''    #empty string to store data in
        clientsocket, address = s.accept()    #accept connection & store IP address
        print(f"Connection from {address} has been established!")    #Write IP that has connected
        clientsocket.send(bytes("Welcome to team GEDI's server!", "utf-8"))   #Send message to client
    #else:
        msg = clientsocket.recv(50)   #Wait to receive a message
        time.sleep(3)
        full_msg += msg.decode()   #Store decrypted message
        print(full_msg)
        if(int(full_msg) == 8):
            motors.Test()
        elif(int(full_msg == x)):
            sqd.task2()
        time.sleep(10)
        socket.close()