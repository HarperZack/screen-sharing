from vidstream import StreamingServer
import threading


LOCAL_IP = '192.168.1.209'

reciever = StreamingServer(LOCAL_IP, 8080)

t = threading.Thread(target=reciever.start_server())
t. start()

while input("") != 'STOP':
    continue

reciever.stop_server()
