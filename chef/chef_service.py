from recommendation_system import RecommendationSystem
from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
from notification_service import Notification
import datetime

class ChefService:
    
    def get_recommendation(self,num_items):
        recommender = RecommendationSystem()
        recommendations = recommender.get_recommendations(num_items)
        response = {"action": "GET_RECOMMENDATION", "data":recommendations}
        return response
    
    def roll_out_menu(self,items_to_rollout):
        items_to_rollout = ','.join(map(str,items_to_rollout))
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"create or replace view item_for_next_day as select * from menu_item where item_id in ({items_to_rollout});"
            db.execute_query(query)
            db.disconnect()
            status = "Menu rolled out successfully"
        except Exception as e:
            status = "Error while rolling out menu"
        response = {"action": "ROLL_OUT_MENU", "status": status}
        return response
    
    def roll_out_finalized_menu(self,items_to_rollout):
        items_to_rollout = ','.join(map(str,items_to_rollout))
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"create or replace view finalized_item_for_next_day as select * from menu_item where item_id in ({items_to_rollout});"
            db.execute_query(query)
            db.disconnect()
            self.send_notification()
            status = "Menu rolled out successfully"
        except Exception as e:
            status = "Error while rolling out menu"
        response = {"action": "ROLL_OUT_FINALIZED_MENU", "status": status}
        return response
    
    def send_notification(self):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = "select item_name from finalized_item_for_next_day;"
            item_names = db.fetch_all(query)
            dishes = [dish_name[0] for dish_name in item_names]
            menu_string = ", ".join(dishes)
            message = f"Tomorrow following items will be prepared -> {menu_string}."
            sender = "CHEF"
            notification = Notification(message,sender)
            notification.send_notification()
            db.disconnect()
        except Exception as e:
            print("Error in notifying employees")
    
    def view_voted_items(self,date):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"select item_id, user_id from voted_item where selection_date = '{date}';"
            voted_items = db.fetch_all(query)
            db.disconnect()
        except Exception as e:
            print("Error in fetching voted items")
        response = {"action": "VIEW_VOTED_ITEMS", "data": voted_items}
        return response