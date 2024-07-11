from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
import datetime
from sentiment_analyzer import SentimentAnalyzer


class EmployeeService:
    
    def vote_for_food_item(self, data):
        try:
            selection_date = str(datetime.datetime.today().date())
            for item_id in data['items_to_vote']:
                print(item_id)
                db = DatabaseConnection(DB_CONFIG)
                db.connect()
                query = '''insert into voted_item (user_id,item_id,selection_date) values (%s,%s,%s)'''
                values = (data['user_id'], item_id, selection_date)
                db.execute_query(query, values)
                db.disconnect()
            status = "Food item voted successfully"
        except Exception as e:
            status = "Error in next day menu items"
        response = {"action": "VOTE_FOR_FOOD_ITEM", "status": status}
        return response