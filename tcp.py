import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
# client.send(b"GET / HTTP/1.1\r\nHOST: 127.0.0.1\r\n\r\n")
client.send(b"Test is test!")
# receive some data
response = client.recv(4096)
print (response)