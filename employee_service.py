from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
import datetime
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
    
    def view_next_day_menu(self):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = f"select item_id,item_name,price,availability_status,item_category from item_for_next_day;"
            next_day_menu = db.fetch_all(query)
            db.disconnect()
            return next_day_menu
        except Exception as e:
            print(e)
            status = "Error in next day menu items"
        return status
    
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
            print(e)
            status = "Error in next day menu items"
        return status
    
    def view_notification(self):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            yesterday_date = str((datetime.datetime.today() - datetime.timedelta(days=1)).date())
            query = f"select message from notification where notification_date >= %s;"
            values = (yesterday_date,)
            notification = db.fetch_all(query,values)
            db.disconnect()
            return notification
        except Exception as e:
            print(e)
            status = "Error in fetching notification"
        return status