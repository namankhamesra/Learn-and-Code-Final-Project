import socket
from commons.literals import SERVER_IP, SERVER_PORT, BUFFER_SIZE
from role_based_menu import RoleBasedMenu

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        print(f"Connected to server at {self.server_ip}:{self.server_port}")

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))
        response = self.client_socket.recv(BUFFER_SIZE).decode('utf-8')
        return response

    def close(self):
        self.client_socket.close()
        print("Connection closed")

def main():
    client = Client(SERVER_IP, SERVER_PORT)
    client.connect()

    try:
        inClient = True
        while inClient:
            if not inClient:
                break
            email = input("Enter your email to login to the system: ")
            response = client.send_message(email)
            if(response.lower() == "admin"):
                RoleBasedMenu.admin_menu()
            elif(response.lower() == "chef"):
                RoleBasedMenu.chef_menu()
            elif(response.lower() == "employee"):
                RoleBasedMenu.employee_menu()
            else:
                print(response)
            
            choice = input("\nDo you want to continue with the system (if not enter exit): ")
            if(choice.lower() == "exit"):
                inClient = False
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()
