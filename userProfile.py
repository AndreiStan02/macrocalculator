from enum import Enum

class ActivityFactor(Enum):
    LIGHT = 1,
    MODERATE = 2,
    VERY = 3

class UserProfile:
    def __init__(self, name, weight, age, height, gender, activity, fat_per):
        self.name = name
        self.weight = weight
        self.age = age
        self.height = height
        self.gender = gender
        self.activity = activity
        self.fat_per = fat_per
        self.tdee = get_tdee(self)
        self.all_measures = []
        self.week_measures = []

    def update_weight(self, new_weight):
        self.weight = new_weight
        self.tdee = get_tdee(self)
        return self.tdee

    def update_fat_per(self, new_fat):
        self.fat_per = new_fat


def get_tdee(profile):
    activity_factor = 0
    match profile.activity:
        case ActivityFactor.LIGHT:
            activity_factor = 1.375
        case ActivityFactor.MODERATE:
            activity_factor = 1.55
        case ActivityFactor.VERY:
            activity_factor = 1.725
        case _:
            raise Exception("no proper activity factor")

    if profile.gender == "male":
        return (10 * profile.weight + 6.25 * profile.height - 5 * profile.age + 5) * activity_factor
    return (10 * profile.weight + 6.25 * profile.height - 5 * profile.age - 161) * activity_factor


#yo = UserProfile("andrei", 80, 23, 178, "male", ActivityFactor.MODERATE, 22)
#print(yo.tdee)