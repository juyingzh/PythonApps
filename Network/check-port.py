import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
try:
  sk.connect(('107.182.30.66',28389))
  print('Server port 28389 OK!')
except Exception:
  print('Server port 28389 not connect!')
sk.close()
