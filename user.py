import csv
from PyInquirer import prompt

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"Add user - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    name = infos["name"]
    with open("users.csv", 'a', newline='') as csvfile:
        new_user = csv.writer(csvfile)
        new_user.writerow([name])
    print("New User Added !")
    return