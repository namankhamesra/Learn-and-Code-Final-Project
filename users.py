from database.db_connection import DatabaseConnection
from commons.literals import *

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
