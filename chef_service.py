from recommendation_system import RecommendationSystem
from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
import datetime

class ChefService:
    
    def get_recommendation(self,num_items):
        recommender = RecommendationSystem()
        recommendations = recommender.get_recommendations(num_items)
        return recommendations
    
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
            print(e)
            status = "Error while rolling out menu"
        return status
    
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
            print(e)
            status = "Error while rolling out menu"
        return status
    
    def send_notification(self):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = "select item_name from finalized_item_for_next_day;"
            item_names = db.fetch_all(query)
            dishes = [dish_name[0] for dish_name in item_names]
            menu_string = ", ".join(dishes)
            menu_string = f"Tomorrow following items will be prepared -> {menu_string}."
            current_date = str(datetime.datetime.today().date())
            query = "insert into notification (message, notification_date, notification_from) values (%s,%s,%s);"
            values = (menu_string, current_date, "CHEF")
            db.execute_query(query, values)
            db.disconnect()
            print("Notified employees Successfully")
        except Exception as e:
            print(e)
            print("Error in notifying employees")
    
    def view_voted_items(self,date):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"select item_id, user_id from voted_item where selection_date = '{date}';"
            voted_items = db.fetch_all(query)
            db.disconnect()
            return voted_items
        except Exception as e:
            print(e)
            status = "Error in fetching voted items"
        return status