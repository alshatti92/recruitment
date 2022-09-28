# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
from operator import ge
from platform import python_branch
from tkinter import N


def get_skills():
   return  ["python" , "c++" , "Javascript" , "Juggling" , "Running" , "Eating"]

print(get_skills())


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    # print (skills)
    for index, skill in enumerate(skills,1):
     print (f"{index}. {skill}")

skills = get_skills()
show_skills(skills)
# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    user_skills1 = int(input ("choose a skill: "))
    show_skills(skills)
    user_skills2 = int(input ("please choose another skill: "))
    user_skills1 = skills[user_skills1 - 1]
    user_skills2 = skills[user_skills2 - 1]
    user_skills = [user_skills1 , user_skills2]
    print(user_skills)
    return user_skills

# it can be summurised by adding steps 4,5,6,7 to the return directly.
skills = get_skills()
get_user_skills(skills)


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills): 
    cv = {}
    cv["name"] = input ("whats your name? ")
    cv["age"] = int(input ("how old are you? "))
    cv["experience"] = int (input("how many years of experience do you have? "))
    cv["skills"] = get_user_skills(skills)
    print (cv)
    return cv
    
    
get_user_cv(get_skills())
    # why this is wrong? person =  {
    #     "name": input ("whats your name?  "),
    # "age": input (" how old are you? "),
    # "experience": input ("how many years of experience do you have? "),
    # "skills": "get_user_skills(skills)"
    # }
    # print (person)


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 >= cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"]:
        return True
    else:
        return False


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions: ")
    skills = get_skills()
    user_cv = get_user_cv(skills)
    is_accepted = check_acceptance(user_cv, "reactjs")
    if is_accepted:
        print (f"you are qualified, {user_cv['name']}")
    else:
        print ("shoof another company")
    


if __name__ == "__main__":
    main()
