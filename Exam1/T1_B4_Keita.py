import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

"""
MENU TOBE SHOWN
"""
def show_menu():
    print("Select a task to perform:")
    print("\t1. Compute BMI")
    print("\t2. Compute BAI")
    print("\t3. Compute RFM")
    print("\t4. Exit")

    choice = input("Which task would you like to perform? ")

    if(not is_number(choice)):
        print("Please enter a valid value.")
        exit()

    else:
        return int(choice)


"""
Body Mass Index (BMI) SECTION
"""
def compute_bmi():
    height = input("What is your height in inches? ")
    weight = input("What is your weight in pound? ")

    if(not(is_number(height)) or not(is_number(weight))):
        print("Please enter valid values.")
        exit()

    else:
        BMI_FACTOR = 703
        Underweight = 18.8
        
        weight = float(weight)
        height = float(height)

        bmi = (BMI_FACTOR * weight)/(height**2)
        category = ""

        if(bmi < Underweight):
            category = "Underweight"

        elif(bmi >= 18.5 and bmi<=24.9):
            category = "Healthy"

        elif(bmi >= 25 and bmi<=29.9):
            category = "Overweight"

        elif(bmi > 30):
            category = "Obese"

    print("BMI\t\tCategory")
    print("{:.2f}\t\t{}\n".format(bmi, category))


"""
Body Adiposity Index (BAI) SECTION
"""
def bai_classification_women(bai_value, age):

    category = ""

    if(age >= 20 and age <=39):
        if(bai_value<21):
            category = "Underweight"

        elif(bai_value>=21 and bai_value<=33):
            category = "Healthy"
            
        elif(bai_value > 33 and bai_value <=39):
            category = "Overweight"

        elif(bai_value > 39):
            category = "Obese"

    elif(age >= 40 and age <=59):
        if(bai_value<23):
            category = "Underweight"

        elif(bai_value>=23 and bai_value<=35):
            category = "Healthy"
            
        elif(bai_value > 35 and bai_value <=41):
            category = "Overweight"          

        elif(bai_value > 41):
            category = "Obese"

    elif(age >= 60 and age <=79):
        if(bai_value < 25):
            category = "Underweight"

        elif(bai_value>=25 and bai_value<=38):
            category = "Healthy"
            
        elif(bai_value > 38 and bai_value <=43):
            category = "Overweight"          

        elif(bai_value > 43):
            category = "Obese"

    return category


# BMI Category for MEN
def bai_classification_men(bai_value, age):

    category = ""

    if(age >= 20 and age <=39):
        if(bai_value<8):
            category = "Underweight"

        elif(bai_value>=8 and bai_value<=21):
            category = "Healthy"
            
        elif(bai_value > 21 and bai_value <=26):
            category = "Overweight"

        elif(bai_value > 26):
            category = "Obese"

    elif(age >= 40 and age <=59):
        if(bai_value<11):
            category = "Underweight"

        elif(bai_value>=11 and bai_value<=23):
            category = "Healthy"
            
        elif(bai_value > 23 and bai_value <=29):
            category = "Overweight"          

        elif(bai_value > 29):
            category = "Obese"

    elif(age >= 60 and age <=79):
        if(bai_value < 13):
            category = "Underweight"

        elif(bai_value>=13 and bai_value<=25):
            category = "Healthy"
            
        elif(bai_value > 25 and bai_value <=31):
            category = "Overweight"          

        elif(bai_value > 31):
            category = "Obese"

    return category

def compute_body_adiposity_index():

    age = input("What is your age in years? ")
    height = input("What is your height in meter? ")
    hipCircumference = input("What is your HipCircumference in centimeter? ")
    sex = input("What is your gender(Men/Women)? ")

    if(not(is_number(age)) or not(is_number(height) or not(is_number(hipCircumference)))):
        print("Please enter valid values.")
        exit()

    else:
        category = ""
        age = int(age)
        height = float(height)
        hipCircumference = float(hipCircumference)
        CONSTANT_SUSTRACT = 8

        bai_value = (hipCircumference/(math.pow(height, 1.5))) - CONSTANT_SUSTRACT

        if(sex.lower() == "woman" or sex.lower() == "women" or sex.lower() == "w"):
            category = bai_classification_women(bai_value, age)

        elif(sex.lower() == "man" or sex.lower() == "men" or sex.lower() == "m"):
            category = bai_classification_men(bai_value, age)

    print("BAI\t\tCategory")
    print("{:.2f}\t\t{}\n".format(bai_value, category))


"""
Relative Fat Mass (RFM) SECTION
"""
def compute_rfm_males(height, waistCircumference):

    CONSTANT_SUSTRACT_MALES = 64
    MULTIPLY_CONSTANT = 20

    percent_fat = CONSTANT_SUSTRACT_MALES - ((MULTIPLY_CONSTANT * height)/waistCircumference)

    return percent_fat

def compute_rfm_females(height, waistCircumference):

    CONSTANT_SUSTRACT_FEMALES = 76
    MULTIPLY_CONSTANT = 20

    percent_fat = CONSTANT_SUSTRACT_FEMALES - ((MULTIPLY_CONSTANT * height)/waistCircumference)

    return percent_fat


def rfm_classification_for_females(percent_fat):

    category = ""

    if(percent_fat < 0.1):
        category = "Underweight"

    elif(percent_fat >= 0.1 and percent_fat <= 0.13):
        category = "Low"

    elif(percent_fat >= 0.14 and percent_fat <= 0.2):
        category = "Athletic"

    elif(percent_fat >= 0.21 and percent_fat <= 0.24):
        category = "Fit"

    elif(percent_fat >= 0.25 and percent_fat <= 0.31):
        category = "Average"

    elif(percent_fat >= 0.32):
        category = "Obese"

    return category


def rfm_classification_for_males(percent_fat):

    category = ""

    if(percent_fat < 0.02):
        category = "Underweight"

    elif(percent_fat >= 0.02 and percent_fat <= 0.05):
        category = "Low"

    elif(percent_fat >= 0.06 and percent_fat <= 0.13):
        category = "Athletic"

    elif(percent_fat >= 0.14 and percent_fat <= 0.17):
        category = "Fit"

    elif(percent_fat >= 0.18 and percent_fat <= 0.24):
        category = "Average"

    elif(percent_fat >= 0.25):
        category = "Obese"

    return category


def compute_rfm():
    
    sex = input("What is your gender(Male/Female)? ")
    height = input("What is your height in inches? ")
    waistCircumference = input("What is your Waist Circumference in inches? ")

    if(not(is_number(height)) or not(is_number(waistCircumference))):
        print("Please enter valid values.")
        exit()

    else:
        category = ""
        height = float(height)
        waistCircumference = float(waistCircumference)
        sex = sex.lower()
        percent_fat = 0

        if(sex == "females" or sex == "female" or sex == "woman" or sex == "f" or sex == "w"):
            percent_fat = compute_rfm_females(height, waistCircumference)
            category = rfm_classification_for_females(percent_fat)

        elif(sex == "males" or sex == "male" or sex == "man" or sex == "f" or sex == "m"):
            percent_fat = compute_rfm_males(height, waistCircumference)
            category = rfm_classification_for_males(percent_fat)      

    print("RFM\t\tCategory")
    print("{:.2f}\t\t{}\n".format(percent_fat, category))


"""
FINAL FUNCTION TO COMPUTE USER's CHOICE
"""

def execute_user_choice(choice):
    if(choice == 1):
        print("Your Choice: BMI Computation")
        compute_bmi()

    elif(choice == 2):
        print("Your Choice: BAI Computation")
        compute_body_adiposity_index()

    elif(choice == 3):
        print("Your Choice: RFM Computation")
        compute_rfm()

    elif(choice == 4):
        exit()

    else:
        print("Please Make a valid choice")
        exit()

if __name__ == "__main__":

    user_choice = show_menu()

    execute_user_choice(user_choice)