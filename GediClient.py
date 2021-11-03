import socket
import variables
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.22", 65530))

msg = s.recv(50)
print(msg.decode("utf-8"))
time.sleep(10)
#test = 5

while 1:
    if int(variables.command) > 0:
        print(variables.command)
        time.sleep(3)
        en_task = variables.command.encode("utp-8")
        print("Encoded")
        s.send(en_task)
        print("Sent")
        #s.send(bytes(task, "utf-8"))
        
    #elif test == 5:
        #str_test = str(test)
        #enc_test = str_test.encode("utf-8")
        #s.send(enc_test)
        time.sleep(10)
        s.close()

    else:
        print(variables.command)
        print("Else")
        msg = s.recv(50)
        time.sleep(5)

    task = variables.command
    print(task)