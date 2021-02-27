# Question1---------------Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health
# Question1---------------risk from Table 1 of the person and add them as 3 new columns
# Question2 --------------Count the total number of overweight people using ranges in the column BMI Category of Table 1
                    # !!!! In line number 42 we are checking the condition for Question 2

# user data storing in variable
users_data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg":85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166,"WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female","HeightCm": 167, "WeightKg": 82}
    ]

# we will store final data in final_data list
final_data = []
# creating a dict
new_dict = {}
over_weight_people_count = 0
for each_user_data in users_data:
    # assign each user weight to a variable -->weight
    weight = each_user_data['WeightKg']
    # assign each user height to a variable -->height
    height = each_user_data['HeightCm']
    # converting the heigth cms to mts
    height_to_cms = height/100
    new_dict['Gender'] = each_user_data['Gender']
    new_dict['HeightCm'] = each_user_data['HeightCm']
    new_dict['WeightKg'] = each_user_data['WeightKg']
    # calculating the BMI 
    new_dict['BMI'] = weight/(height_to_cms**2)
    # condition for BMI Range and Health risk
    if(new_dict['BMI']<=18.4):
        new_dict['BMI_Category'] = 'Underweight'
        new_dict['Health_risk'] = 'Malnutrition risk'
    elif(new_dict['BMI']>=18.5 and new_dict['BMI'] <= 24.9):
        new_dict['BMI_Category'] = 'Normal weight'
        new_dict['Health_risk'] = 'Low risk'
    elif(new_dict['BMI']>=25 and new_dict['BMI'] <= 29.9):
        new_dict['BMI_Category'] = 'Overweight'
        # here we are also checking the overweight count for ----------------> QUESTION 2
        over_weight_people_count += 1
        new_dict['Health_risk'] = 'Enhanced risk'
    elif(new_dict['BMI']>=30 and new_dict['BMI'] <= 34.9):
        new_dict['BMI_Category'] = 'Moderately obese'
        new_dict['Health_risk'] = 'Medium risk'
    elif(new_dict['BMI']>=35 and new_dict['BMI'] <= 39.9):
        new_dict['BMI_Category'] = 'Severely obese'
        new_dict['Health_risk'] = 'High risk'
    elif(new_dict['BMI']>=40):
        new_dict['BMI_Category'] = 'Very severely obese'
        new_dict['Health_risk'] = 'Very high risk'
    # here we are appending the each user data to a list(final_data) and we are making the new_dict empty  
    final_data.append(new_dict)
    new_dict = {}

print(final_data)
print(over_weight_people_count)