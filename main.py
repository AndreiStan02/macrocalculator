import plotext as plt
from session import Session
from userProfile import ActivityFactor

session = Session()
user_exists = False

def log_create_acc():
    while(True):
        print("Write 'log' or 'create' to login or create and account!")
        command = input()
        if command == "log":
            user_loged = True
            print("Write your user name to log in, or exit to go back")
            while(True):
                user_name = input()
                if user_name == "exit":
                    break

                session.logIn(user_name)
                if session.currentProfile != None:
                    break
                else:
                    print("User not found, try again")
            register_data()
            break
        elif command == "create":
            while(True):
                print("To create an account we are going to ask for some personal information.")
                print("What is you name?")
                user_name = input()
                if user_name == "exit":
                    break
                for tupple in session.profiles:
                    if tupple[0] == user_name:
                        user_exists = True
                        print("User already exists")

                if user_exists: break
                    
                print("What is you weight?")
                user_weight = int(input())
                if user_weight == "exit":
                    break
                print("What is you age?")
                user_age = int(input())
                if user_age == "exit":
                    break
                print("What is you height?")
                user_height = int(input())
                if user_height == "exit":
                    break
                print("What is you gender?")
                user_gender = input()
                if user_gender == "exit":
                    break
                print("How much do you excercise? Please use 'LIGHT', 'MODERATE' or 'VERY'")
                user_activity = input()
                if user_activity == "exit":
                    break
                print("What is you fat percentage?")
                user_fat_per = float(input())
                if user_fat_per == "exit":
                    break
                print("What is you goal fat percentage?")
                user_goal_per = float(input())
                if user_goal_per == "exit":
                    break
                session.createProfile(user_name, user_weight, user_age, user_height, user_gender, user_activity, user_fat_per, user_goal_per)
                print("Profile created")
                session.logIn(user_name)
                break
            break
        print("Wrong order, try again.")

def register_data():
    print("Tell us your current weight")
    new_weight = float(input())
    print("Tell us your current body fat percentage")
    new_fat_per = float(input())
    session.update_weight_currentprofile(new_weight, new_fat_per)

def show_status():
    pass
    
log_create_acc()
show_status()