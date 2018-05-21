import socket                                                                   #import from library

IP = "127.0.0.1"                                                                # set the ip for socket            
PORT = 8080                                                                     # set the port number up to 65536
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


# the below is from Yioni and he said it is a refactored code from the above - it is a bit different to the above as I created the loop myself as i wanted on the above and it's different from the below
    
import socket

IP = '0.0.0.0'
PORT = 8080
MAXIMUM_QUEUE_SIZE = 0
BUFFER_SIZE = 2048


def respond(client_socket, client_ip_and_port):                                 #this creates an internal server
    request = client_socket.recv(BUFFER_SIZE).decode()                          #to create an internal server we need to return headers, status codes, and the html
    response_headers = "HTTP/1.1 200 OK\n\n"
    response_body = "Your request was:\n" + request
    encoded_response = (response_headers + response_body).encode()
    client_socket.send(encoded_response)


def serverloop():
    listening_socket = socket.socket()
    listening_socket.bind((IP, PORT))
    listening_socket.listen(MAXIMUM_QUEUE_SIZE)

    while True:
        (client_socket, client_ip_and_port) = listening_socket.accept()
        respond(client_socket, client_ip_and_port)
        client_socket.close()


if __name__ == '__main__':  # is this file executed directly (not just imported)
    print('Server launched on %s:%s, press ctrl+c to kill the server'
          % (IP, PORT))
    serverloop()