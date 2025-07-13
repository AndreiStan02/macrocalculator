import json

from userProfile import UserProfile, ActivityFactor

class Session:
    def __init__(self):
        self.profiles = []
        self.currentProfile = None
        self.get_profiles()

    def createProfile(self, name, weight, age, height, gender, activity, fat_per, goal_per):
        user = {
            "name": name,
            "weight":weight,
            "age":age,
            "height":height,
            "gender":gender,
            "activity":activity,
            "fat_per":fat_per,
            "goal_per":goal_per,
            "all_measures":[(weight,fat_per)],
            "week_measures":[(weight,fat_per)],
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
            aux_profile = UserProfile(profile["name"], profile["weight"], profile["age"], profile["height"], profile["gender"], profile["activity"], profile["fat_per"], profile["goal_per"], profile["all_measures"], profile["week_measures"])
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