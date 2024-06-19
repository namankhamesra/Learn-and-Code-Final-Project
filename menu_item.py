from database.db_connection import DatabaseConnection
from commons.literals import *

class MenuItem:
    def __init__(self, item_name, price, availability_status, item_category):
        self.item_name = item_name
        self.price = price
        self.availability_status = availability_status
        self.item_category = item_category

    def add_menu_item(self):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = '''
        insert into menu (item_name, price, availability_status, item_category) values (%s,%s,%s,%s);
        '''
        values = (self.item_name, self.price, self.availability_status, self.item_category)
        db.execute_query(query, values)
        db.disconnect()
        