import sys
sys.path.append("..")
from authentication import AuthService

class ClientHandler:
    def __init__(self, client_socket, client_address):
        self.client_socket = client_socket
        self.client_address = client_address

    def handle(self):
        print(f"Accepted connection from {self.client_address}")
        try:
            while True:
                email = self.client_socket.recv(1024).decode('utf-8')
                authenticate_user = AuthService()
                user_details = authenticate_user.login(email)
                if len(user_details) == 1:
                    user_role = user_details[0][2]
                    response = user_role
                else:
                    print(f"User Not Authenticated")
                    response = "You are not registered to the system"
                    
                self.client_socket.send(response.encode('utf-8'))
        except (ConnectionResetError, ConnectionAbortedError):
            pass
        finally:
            print(f"Connection from {self.client_address} has been closed")
            self.client_socket.close()
