import socket

s =socket.socket()

host = socket.gethostname()
port =5432

s.connect((host,port))

while True:
    data = raw_input ('Enter your message : ')
    s.sendall(data)
    print ("Wait for client to respond")
    data=s.recv(1024)
    print 'Client: ' , data
    if data == 'end':
        break
s.close()

