import socket                                                                   #import from library

IP = "127.0.0.1"                                                                # set the ip for socket            
PORT = 1235                                                                     # set the port number up to 65536
MAXIMUM_QUEUE_SIZE = 0                                                          # set the amount of requests to be queued before rejecting
BUFFER_SIZE = 2048


listening_socket = socket.socket()                                              # uses socket library and starts the function socket
listening_socket.bind((IP, PORT))                                               # as name implies it links ip and port together

listening_socket.listen(MAXIMUM_QUEUE_SIZE)                                     # starts the listen function including the queue size
print("Hello, I'm waiting for a connection")                                    # this prints a message



(client_socket, client_ip_and_port) = listening_socket.accept()                 # this creates a socket using the ip and port and accepts the listening socket
# (client_ip, client_port) = client_ip_and_port                                 # unpacks the tuple into ip and port - but dont need this line with the while loop
    
initial_response = "Hi there, what's up\n".encode()                             # creates a response
client_socket.send(initial_response)                                            # sends response
while True:                                                                     # the while loop makes sure it goes back to the below
    client_message = client_socket.recv(BUFFER_SIZE).decode()                   # recieves back but specifies how many bits max we are willing to recive - as we are recieving we need to decode
    echo_response = ("You said: " + client_message).encode()                    # creates response and encodes it
    # client_message != "\n":
    client_socket.send(echo_response)                                           # sends response   
                                                  
    # client_socket.close()                                                     # this will close it
