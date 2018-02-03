import socket 

host = '' 
port = 50002
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 

while 1:
    client, address = s.accept() 
    print "Client connected."
    client.send("Hello!\n") 

    while 1: 
        data = client.recv(size).rstrip('\r\n')
        print data
        if data: 
            if data=="quit":
                client.send("Bye!\n")
                client.close()
                break
            else:
                client.send("You just said: " + data + "\n") 

