import json

import plotext as plt
from session import Session
from userProfile import ActivityFactor, get_cal, get_goal_time, calculate_cals

session = Session()

def log_create_acc():
    user_exists = False
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

                if user_exists == True: break
                    
                print("What is you weight?")
                user_weight = float(input())
                if user_weight == "exit":
                    break
                print("What is you age?")
                user_age = int(input())
                if user_age == "exit":
                    break
                print("What is you height?")
                user_height = float(input())
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
    
    days_left = session.currentProfile.goal_time
    with open('users.json', 'r') as f:
        data = json.load(f)

    for profile in data:
        if profile["name"] == session.currentProfile.name:
            profile["goal_time"] -= 1

    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)


    if len(session.currentProfile.week_measures) >= 7:
        weight = [x[0] for x in session.currentProfile.week_measures]
        fat_per = [x[1] for x in session.currentProfile.week_measures]
        x = list(range(1, len(session.currentProfile.week_measures) + 1))

        plt.clear_figure()  # clear any previous plot
        plt.plot(x, weight, marker='dot')
        plt.title("Weight Progress")
        plt.xlabel("Measurement")
        plt.ylabel("Weight (kg)")
        plt.show()

        # --- Body Fat Plot ---
        plt.clear_figure()  # clear again for next plot
        plt.plot(x, fat_per, marker='dot', color='red')
        plt.title("Body Fat Percentage Progress")
        plt.xlabel("Measurement")
        plt.ylabel("Body Fat (%)")
        plt.show()

        with open('users.json', 'r') as f:
            data = json.load(f)

        for profile in data:
            if profile["name"] == session.currentProfile.name:
                profile["cal_intake"] = get_cal(session.currentProfile)
                session.currentProfile.cal_intake = get_cal(session.currentProfile)
                profile["week_measures"] = []

        with open('users.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("You completed a week, this is your week progress!!")


    current_cals = session.currentProfile.cal_intake
    
    print("You need to eat ",int(current_cals)," kcals for ",int(days_left)," days to get to your goal, KEEP IT UP!!!!")
    
log_create_acc()
show_status()