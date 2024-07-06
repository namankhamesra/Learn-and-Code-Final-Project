import datetime
from commons.literals import DB_CONFIG
from database.db_connection import DatabaseConnection


class Notification:
    def __init__(self, message, sender):
        self.message = message
        self.sender = sender

    def send_notification(self):
        try:
            db = DatabaseConnection(DB_CONFIG)
            db.connect()
            current_date = str(datetime.datetime.today().date())
            query = "insert into notification (message, notification_date, notification_from) values (%s,%s,%s);"
            values = (self.message, current_date, self.sender)
            db.execute_query(query, values)
            db.disconnect()
        except Exception as e:
            print("Error while sending notification")