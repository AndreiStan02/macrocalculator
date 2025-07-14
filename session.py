import json

from userProfile import UserProfile, ActivityFactor, get_goal_time

class Session:
    def __init__(self):
        self.profiles = []
        self.currentProfile = None
        self.get_profiles()

    def createProfile(self, name, weight, age, height, gender, activity, fat_per, goal_per):
        if activity == "LIGHT":
            actual_activity = ActivityFactor.LIGHT
        elif activity == "MODERATE":
            actual_activity = ActivityFactor.MODERATE
        else:
            actual_activity = ActivityFactor.VERY 
        tdee = self.get_tdee(actual_activity, gender, weight, height, age)
        
        user = {
            "name": name,
            "weight":weight,
            "age":age,
            "height":height,
            "gender":gender,
            "activity":activity,
            "fat_per":fat_per,
            "goal_per":goal_per,
            "goal_time": int(((weight-(weight + (weight - (weight*(fat_per/100))) / (1 - goal_per)))/0.5)*7),
            "cal_intake": self.get_cal(weight,fat_per, goal_per, int(((weight-(weight + (weight - (weight*(fat_per/100))) / (1 - goal_per)))/0.5)*7), tdee),
            "all_measures":[(weight,fat_per)],
            "week_measures":[(weight,fat_per)],
            "last_day":"",
        }
   
        with open('users.json', 'r') as f:
            data = json.load(f)

        data.append(user)

        with open('users.json', 'w') as f:
            json.dump(data, f, indent=4)
        self.get_profiles()

    def logIn(self, name):
        for tupple in self.profiles:
            if tupple[0] == name:
                self.currentProfile = tupple[1]
            else:
                raise Exception("No user with this name exists")

    def get_profiles(self):
        with open("users.json", "r") as file:
            data = json.load(file)
        for profile in data:
            aux_profile = UserProfile(profile["name"], profile["weight"], profile["age"], profile["height"], profile["gender"], profile["activity"], profile["fat_per"], profile["goal_per"],profile["goal_time"],profile["cal_intake"],profile["all_measures"], profile["week_measures"])
            self.profiles.append((profile["name"], aux_profile))

    def update_weight_currentprofile(self,new_weight, new_fat_per):
        with open('users.json', 'r') as f:
            data = json.load(f)

        for profile in data:
            if profile["name"] == self.currentProfile.name:
                profile["weight"] = new_weight
                profile["fat_per"] = new_fat_per
                profile["all_measures"].append((new_weight, new_fat_per))
                profile["week_measures"].append((new_weight, new_fat_per))

        with open('users.json', 'w') as f:
            json.dump(data, f, indent=4)
        self.get_profiles()

    def get_tdee(self, activity, gender, weight, height, age):
        activity_factor = 0
        match activity:
            case ActivityFactor.LIGHT:
                activity_factor = 1.375
            case ActivityFactor.MODERATE:
                activity_factor = 1.55
            case ActivityFactor.VERY:
                activity_factor = 1.725
            case _:
                raise Exception("no proper activity factor")

        if gender == "male":
            return (10 * weight + 6.25 * height - 5 * age + 5) * activity_factor
        return (10 * weight + 6.25 * height - 5 * age - 161) * activity_factor

    def get_cal(self, weight, fat_per, goal_per, goal_time, tdee):
        target_weight = (weight - (weight*(fat_per/100))) / (1 - (goal_per/100))
        total_cal = 7700 * (weight - target_weight)
        cal_per_day = total_cal/goal_time
        return tdee - cal_per_day