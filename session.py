from userProfile import UserProfile, ActivityFactor

class Session:
    def __init__(self):
        self.profiles = {}

    def createProfile(self, name, weight, age, height, gender, activity, fat_per):
        new_profile = UserProfile(name, weight, age, height, gender, activity, fat_per)
        if self.profiles[new_profile.name]:
            raise Exception("User already exists")
        self.profiles.update({new_profile.name: new_profile})