from enum import Enum

class ActivityFactor(Enum):
    LIGHT = 1,
    MODERATE = 2,
    VERY = 3

class UserProfile:
    def __init__(self, name, weight, age, height, gender, activity, fat_per, goal_per, goal_time, cal_intake,all_measures = [], week_measures = []):
        self.name = name
        self.weight = weight
        self.age = age
        self.height = height
        self.gender = gender
        if activity == "LIGHT":
            self.activity = ActivityFactor.LIGHT
        elif activity == "MODERATE":
            self.activity = ActivityFactor.MODERATE
        else:
            self.activity = ActivityFactor.VERY 
        self.fat_per = fat_per
        self.goal_per = goal_per
        self.goal_time = goal_time
        self.tdee = get_tdee(self)
        self.cal_intake = cal_intake
        if all_measures == []:
            self.all_measures = [(weight, fat_per)]
        else:
            self.all_measures = all_measures
        if week_measures == []:
            self.week_measures = [(weight, fat_per)]
        else:
            self.week_measures = week_measures


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

def get_cal(profile):
    target_weight = (profile.weight - (profile.weight*(profile.fat_per/100))) / (1 - (profile.goal_per/100))
    total_cal = 7700 * (profile.weight - target_weight)
    cal_per_day = total_cal/profile.goal_time
    return profile.tdee - cal_per_day

def get_goal_time(profile):
    target_weight = (profile.weight - (profile.weight*(profile.fat_per/100))) / (1 - profile.goal_per)
    return ((profile.weight-(profile.weight + target_weight))/0.5)*7

def calculate_cals(profile):
    total_weight = 0
    avr_weight = 0
    espected_weight = profile.week_measures[0][0] - 0.5
    for measure in profile.week_measures:
        total_weight += measure[0]
    avr_weight = total_weight/7
    if abs(espected_weight - avr_weight) >= 0.5:
        if espected_weight > avr_weight:
            profile.tdee += 100
        else:
            profile.tdee -= 100
    profile.week_measures = []