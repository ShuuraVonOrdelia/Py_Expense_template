import csv
from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]


def get_existing_users():
    with open("users.csv", "r") as users_file:
        reader = csv.reader(users_file)
        return [row[0] for row in reader]

def new_expense(*args):
    infos = prompt(expense_questions)
    amount = infos["amount"]
    label = infos["label"]
    existing_users = get_existing_users()

    spender = None
    while spender not in existing_users:
        spender = input("Enter an existing user as the spender: ")

    with open("expense_report.csv", 'a', newline='') as csvfile:
        expense = csv.writer(csvfile)
        expense.writerow([amount, label, spender])

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True