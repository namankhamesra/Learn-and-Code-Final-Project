from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
import datetime
import json

from sentiment_analyzer import SentimentAnalyzer


class EmployeeService:
    
    def provide_feedback(self, data):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        feedback_date = str(datetime.datetime.today().date())
        sentiment_analyzer = SentimentAnalyzer()
        sentiment_score = sentiment_analyzer.analyze_sentiment(data['comment'])
        query = '''
        insert into feedback (user_id, item_id, comment, rating, sentiment_score, feedback_date) values (%s,%s,%s,%s,%s,%s);
        '''
        values = (data['user_id'], data['item_id'],data['comment'],data['rating'],sentiment_score,feedback_date)
        db.execute_query(query, values)
        db.disconnect()
        status = "Item added successfully"
        return status
    
    def view_next_day_menu(self,data):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()
        query = '''
        select Distinct item_id, item_name, price, type from item_for_next_day n join item_category i on n.item_category = i.id;
        '''
        next_day_items = db.fetch_all(query)
        db.disconnect()
        return next_day_items
    
    def vote_for_food_item(self, item_ids):
        db = DatabaseConnection(DB_CONFIG)
        db.connect()