import datetime
from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection
from sentiment_analyzer import SentimentAnalyzer

class Feedback:

    def provide_feedback(self, data):
        try:
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
            status = "Feedback provided successfully"
        except Exception as e:
            status = "Error while providing feedback"
        response = {"action": "PROVIDE_FEEDBACK", "status": status}
        return response