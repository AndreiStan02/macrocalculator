import json

from userProfile import UserProfile, ActivityFactor

class Session:
    def __init__(self):
        self.profiles = []
        self.currentProfile = None
        self.get_profiles()

    def createProfile(self, name, weight, age, height, gender, activity, fat_per, goal_per):
        data = {
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

        new_profile = UserProfile(name, weight, age, height, gender, activity, fat_per, goal_per)
        if self.profiles[new_profile.name]:
            raise Exception("User already exists")
        with open('data.json', 'w') as f:
            json.dump(data, f)
        self.get_profiles()

    def logIn(self, name):
        if self.profiles[name]:
            self.currentProfile = self.profiles[name]
        else:
            raise Exception("No user with this name exists")

    def get_profiles(self):
        with open("users.json", "r") as file:
            data = json.load(file)
        for profile in data:
            aux_profile = UserProfile(data.name, data.weight, data.age, data.height, data.gender, data.activity, data.fat_per, data.goal_per, data.all_measures, data.week_measures)
            self.profiles.append((data.name, aux_profile))