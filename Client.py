import socket,cv2,pickle,struct
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverip="192.168.43.51"
serverport=1111
s1.connect( (serverip,serverport) )

data=b""
payload_size=struct.calcsize("Q")
while True:
    while len(data)<payload_size:
        packet=s1.recv(4*1024)
        if not packet:break
        data+=packet
    packed_msg_size=data[:payload_size]
    data=data[payload_size:]
    msg_size=struct.unpack("Q",packed_msg_size)[0]
    while len(data)<msg_size:
        data+=s1.recv(4*1024)
    frame_data=data[:msg_size]
    data=data[msg_size:]
    frame=pickle.loads(frame_data)
    cv2.imshow("video2",frame)
    key=cv2.waitKey(10)
    if key==13:
        break
s1.close()
