from database.db_connection import DatabaseConnection
from commons.literals import *

class MenuItem:
    def __init__(self, item_id=None, item_name=None, price=None, availability_status=None, item_category=None):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.availability_status = availability_status
        self.item_category = item_category

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "price": self.price,
            "availability_status": self.availability_status,
            "item_category": self.item_category,
        }
    
    @classmethod
    def fetch_complete_menu(cls):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = "SELECT * FROM menu_item where is_deleted = 0;"
        menu_items = db.fetch_all(query)
        db.disconnect()
        response = {"action": "FETCH_COMPLETE_MENU", "data":menu_items}
        return response
    
    def get_item_detail_by_id(self,item_id):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = f"SELECT * FROM menu_item where item_id in ({item_id});"
        menu_items = db.fetch_all(query)
        db.disconnect()
        return menu_items