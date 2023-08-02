import math
from OSRSLevels import level_xp_mapping

#This 
def xp_for_level(level):
    if level < 1 or level > 99:
        raise ValueError("Level must be between 1 and 99.")
    return level_xp_mapping[level]


def xp_left():
    global total_xp_needed
    try:
        current_xp = int(input("What is your total xp currently? "))    
        desired_level = int(input("What level are you looking to achieve? "))
        total_xp_needed = xp_for_level(desired_level) - current_xp
    except ValueError as ve:
        print(ve)
        
    print(total_xp_needed)
    
    print(f"To reach level {desired_level}, you need {total_xp_needed} XP. ")
    
def contracts():
    average_xp_per_contract = 4445
    
    total_contracts = total_xp_needed / average_xp_per_contract
    
    rounded_number_of_contracts = math.ceil(total_contracts)
    
    print(f"You have roughly {rounded_number_of_contracts} contracts left until your level")
    
def planks_needed():
    average_plank_xp = 344
    
    planks_user_needs = total_xp_needed / average_plank_xp
    
    rounded_number_of_planks = math.ceil(planks_user_needs)
    
    while True:
        plank_number_question = input("Would you like to know how many planks on average you would need? (yes/no)")
        
        if plank_number_question == "yes":
            print(f"You would need on average {rounded_number_of_planks} planks")
            break
        elif plank_number_question == "no":
            print("Thanks for using the calculator")
            break
        else:
            print("Answer not recognised, please only input yes or no")      
    
def main():
    xp_left()
    contracts()
    planks_needed()
    
main()