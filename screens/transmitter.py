from vidstream import ScreenShareClient
import threading
import restricted

transmitter = ScreenShareClient(restricted.PARENTS_IP, 8080)

t = threading.Thread(target=transmitter.start_stream())
t.start()

while input("") != 'STOP':
    continue

transmitter.stop_stream()
