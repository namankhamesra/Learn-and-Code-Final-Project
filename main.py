from client import Client
from commons.literals import SERVER_IP, SERVER_PORT
from role_based_menu import RoleBasedMenu
import json

def main():
    client = Client(SERVER_IP, SERVER_PORT)
    client.connect()

    try:
        inClient = True
        while inClient:
            if not inClient:
                break
            email = input("Enter your email to login to the system: ")
            response = client.send_message(email)
            response = json.loads(response)
            user_id = response[1]
            user_role = response[0]
            if(user_role.lower() == "admin"):
                while True:
                    request = RoleBasedMenu.admin_menu()
                    if(request == "LOGOUT"):
                        break
                    response = json.loads(client.send_message(request))
                    if(response['action'] == "ADD_MENU_ITEM"):
                        print(response['status'])
                    elif(response['action'] == "UPDATE_AVAILABILITY"):
                        print(response['status'])
                    elif(response['action'] == "DELETE_ITEM"):
                        print(response['status'])
                    elif(response['action'] == "VIEW_FEEDBACK"):
                        print("User Id".ljust(10), "Item Id".ljust(20), "Comment".ljust(40), "Rating".ljust(40), "Sentiment Score".ljust(0))
                        for i in response['feedback']:
                            print(str(i[1]).ljust(10),str(i[2]).ljust(20),str(i[3]).ljust(40),str(i[4]).ljust(40),str(i[5]).ljust(0))
                    elif(response['action'] == "FETCH_COMPLETE_MENU"):
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response['data']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
            elif(user_role.lower() == "chef"):
                while True:
                    request = RoleBasedMenu.chef_menu()
                    if(request == "LOGOUT"):
                        break
                    response = json.loads(client.send_message(request))
                    if(response['action'] == "GET_RECOMMENDATION"):
                        for category in response['data']:
                            print(f"\n----{category.upper()}----")
                            print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                            for i in response['data'][category]:
                                print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    elif(response['action'] == "ROLL_OUT_MENU"):
                        print(response['status'])
                    elif(response['action'] == "FETCH_COMPLETE_MENU"):
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response['data']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    elif(response['action'] == "VIEW_VOTED_ITEMS"):
                        print("Item Id".ljust(10), "User Id".ljust(20))
                        for i in response['data']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20))
                    elif(response['action'] == "ROLL_OUT_FINALIZED_MENU"):
                        print(response['status'])
                    elif(response['action'] == "VIEW_NOTIFICATION"):
                        for message in response['data']:
                            print(message[0])
                    elif(response['action'] == "GENERATE_DISCARD_MENU_ITEM"):
                        print(response['status'])
                    elif(response['action'] == "REVIEW_DISCARDED_ITEM_LIST"):
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Average Rating".ljust(20), "Average Sentiment".ljust(20), "Discard list generation date".ljust(0))
                        for i in response['discarded_items']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    elif(response['action'] == "DELETE_DISCARDED_ITEMS"):
                        print(response['status'])
                    elif(response['action'] == "TAKE_DETAILED_FEEDBACK"):
                        print(response['status'])
                    elif(response['action'] == "VIEW_FEEDBACK"):
                        print("User Id".ljust(10), "Item Id".ljust(20), "Comment".ljust(40), "Rating".ljust(40), "Sentiment Score".ljust(0))
                        for i in response['feedback']:
                            print(str(i[1]).ljust(10),str(i[2]).ljust(20),str(i[3]).ljust(40),str(i[4]).ljust(40),str(i[5]).ljust(0))
                    elif(response['action'] == "VIEW_DETAILED_FEEDBACK"):
                        if(len(response['feedback']) == 0):
                            print("No employees provided feedback till now")
                        else:
                            print("User Id".ljust(10), "Item Id".ljust(20), "Liked".ljust(40), "Not Liked".ljust(40), "Home Recipe".ljust(0))
                            for i in response['feedback']:
                                print(str(i[1]).ljust(10),str(i[2]).ljust(20),str(i[3]).ljust(40),str(i[4]).ljust(40),str(i[5]).ljust(0))
            elif(user_role.lower() == "employee"):
                while True:
                    request = RoleBasedMenu.employee_menu(user_id)
                    if(request == "LOGOUT"):
                        break
                    response = json.loads(client.send_message(request))
                    if(response['action'] == "VIEW_NEXT_DAY_MENU"):
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response['data']['next_day_menu']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    elif(response['action'] == "FETCH_COMPLETE_MENU"):
                        print("Item Id".ljust(10), "Item Name".ljust(20), "Price".ljust(20), "Availability Status".ljust(20), "Item Category".ljust(0))
                        for i in response['data']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(20),str(i[2]).ljust(20),str(i[3]).ljust(20),str(i[4]).ljust(20))
                    elif(response['action'] == "VIEW_NOTIFICATION"):
                        for message in response['data']:
                            print(message[0])
                    elif(response['action'] == "PROVIDE_FEEDBACK"):
                        print(response['status'])
                    elif(response['action'] == "VOTE_FOR_FOOD_ITEM"):
                        print(response['status'])
                    elif(response['action'] == "VIEW_DISCARDED_ITEMS"):
                        print("Item Id".ljust(10), "Item Name".ljust(0))
                        for i in response['discarded_items']:
                            print(str(i[0]).ljust(10),str(i[1]).ljust(0))
                    elif(response['action'] == "PROVIDE_DETAILED_FEEDBACK"):
                        print(response['status'])
            else:
                print(response)
            inClient = False
    except KeyboardInterrupt:
        pass
    finally:
        client.close()

if __name__ == "__main__":
    main()