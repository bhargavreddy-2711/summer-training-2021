import socket,cv2,pickle,struct
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=1111
ip=""

s.bind( (ip,port) )

s.listen(5)

while True:
    client_socket,addr=s.accept()
    print("got connection from: ",addr)
    if client_socket:
        vid=cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame=vid.read()
            a=pickle.dumps(frame)
            message=struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow("video 1",frame)
            key=cv2.waitKey(10)
            if key==13:
                client_socket.close()
