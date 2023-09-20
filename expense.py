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
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    amount = infos["amount"]
    label = infos["label"]
    spender = infos["spender"]

    with open("expense_report.csv", 'a', newline='') as csvfile:
        expense = csv.writer(csvfile)
        expense.writerow([amount, label, spender])

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True