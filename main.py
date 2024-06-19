from authentication import AuthService
from commons.literals import *

def main():
    # Create the Role table if it doesn't exist
    auth_test = AuthService()
    auth_test.login("rydam@gmail.com")

if __name__ == "__main__":
    main()
