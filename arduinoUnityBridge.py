import socket 
import serial

host = '' 
port = 50002
ser = serial.Serial('COM20', 9600)

backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

while 1:
    client, address = s.accept() 
    print "Client connected."
    print ser.readline()
    a0_val = ser.readline()
    client.send(a0_val) 

    while 1: 
        data = client.recv(size).rstrip('\r\n')
        print data
        client.send(a0_val)
        if data: 
            if data=="quit":
                client.send("Bye!\n")
                client.close()
                break
            else:
                client.send("You just said: " + a0_val + "\n")
