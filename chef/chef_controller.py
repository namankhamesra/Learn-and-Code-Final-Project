import json
from datetime import datetime, timedelta

class ChefController:
    
    def get_recommendation(self):
        action = "GET_RECOMMENDATION"
        number_of_items_chef_want = int(input("Enter number of items you want from recommendation system: "))
        item_detail_to_send_to_server = json.dumps({'action': action, 'number_of_items_chef_want': number_of_items_chef_want})
        return item_detail_to_send_to_server
    
    def roll_out_menu(self):
        action = "ROLL_OUT_MENU"
        number_of_items_to_rollout = int(input("Enter number of items you want to roll out for each meal type: "))
        print("Enter all the item_ids you want to roll out: ")
        item_ids = []
        for _ in range(number_of_items_to_rollout*3):
            item_id = int(input(f"Enter item id:"))
            item_ids.append(item_id)
        item_detail_to_send_to_server = json.dumps({'action': action, 'items_to_rollout': item_ids})
        return item_detail_to_send_to_server
    
    def fetch_complete_menu(self):
        action = "FETCH_COMPLETE_MENU"
        item_detail_to_send_to_server = json.dumps({'action': action})
        return item_detail_to_send_to_server
    
    def view_voted_items(self):
        action = "VIEW_VOTED_ITEMS"
        yesterday = (datetime.today() - timedelta(days=1)).date()
        item_detail_to_send_to_server = json.dumps({'action': action, 'date':str(yesterday)})
        return item_detail_to_send_to_server
    
    def roll_out_finalized_menu(self):
        action = "ROLL_OUT_FINALIZED_MENU"
        number_of_items_to_rollout = int(input("Enter number of items you want to roll out for each meal type: "))
        print("Enter all the item_ids you want to roll out: ")
        item_ids = []
        for i in range(number_of_items_to_rollout*3):
            item_id = int(input(f"Enter item id:"))
            item_ids.append(item_id)
        item_detail_to_send_to_server = json.dumps({'action': action, 'items_to_rollout': item_ids})
        return item_detail_to_send_to_server
    
    def view_notification(self):
        action = "VIEW_NOTIFICATION"
        request_from = "CHEF"
        item_detail_to_send_to_server = json.dumps({'action': action, 'data': {"request_from": request_from}})
        return item_detail_to_send_to_server
    
    def generate_discard_menu_item_list(self):
        action = "GENERATE_DISCARD_MENU_ITEM"
        item_detail_to_send_to_server = json.dumps({'action': action})
        return item_detail_to_send_to_server
