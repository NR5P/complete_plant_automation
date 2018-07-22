import socket
from irrigationTimerMainMenu import mainMenu
import time
import threading

host = ""
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


try:
	s.bind((host, port))
except socket.error as e:
	print(str(e))

s.listen(2)

def threaded_client(conn):
	conn.send(str.encode("welcome to blue frog irrigation controller\n"))
	mainMenu(conn)
	conn.send(str.encode("closing connection"))
	conn.close()

def socket_connection():
	while True:
		conn, addr = s.accept()
		socket_obj = threading.Thread(target=threaded_client, args=[conn])
		socket_obj.start()

#create a time out on the port
