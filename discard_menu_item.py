from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection

class DiscardMenu:
    def get_discard_menu_item_list():
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            query = """select f.item_id, item_name, avg(rating) as average_rating, 
            avg(sentiment_score) as average_sentiment from feedback f join menu_item m on f.item_id = m.item_id
            group by f.item_id having average_rating < 2.5 and average_sentiment < 0;"""
            discarded_items = db.fetch_all(query)
            db.disconnect()
            status = "Menu rolled out successfully"
        except Exception as e:
            print(e)
            status = "Error while rolling out menu"
        return status