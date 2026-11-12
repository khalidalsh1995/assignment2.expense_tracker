"""this file shows the menu and reads what the user enters."""


from expense_tracker import ExpenseTracker
from file_persister import FilePersister


class CliUserInterface:
#set up the expense tracker and the file helper.
    def __init__(self):
        self.tracker = ExpenseTracker()
        self.persister = FilePersister()

#show the menu options.
    def dirplay_menu(self):
        print("Expense Tracker")
        print("1- add Expense")
        print("2- show all expenses")
        print("3- filter expenses")
        print("4- save expenses to json")
        print("5- open expenses from json")
        print("6- export expenses to csv")
        print("7- exit")

#run the option the user picks and keep showing the menu until they exit.
    def start_app(self):
        while True:
            self.dirplay_menu()
            choice = input("enter your choice: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.show_expenses()
            elif choice == "3":
                self.filter_expenses()
            elif choice == "4":
                self.save_to_json()
            elif choice == "5":
                self.open_from_json()
            elif choice == "6":
                self.export_to_csv()
            elif choice == "7":
                print("goodbye!")
                break
            else:
                print("invalid choice")


#ask for the expense details(date, category, amount and description) and send them to tracker.
    def add_expense(self):
        date = input("Date (YYYY-MM-DD):  ")
        category = input("category: ")
        amount = input ("amount: ")
        description = input ("dlslescription: ")

        self.tracker.add_expense(date, category, amount, description)
        print("expense added.")


#get all expenses and pass them to the print method.
    def show_expenses(self):
        expenses = self.tracker.get_all_expenses()
        self.print_expenses(expenses)
        

    def print_expenses(self, expenses):
        if len(expenses) == 0:
            print("no expenses to show.")
            return

        for expense in expenses:
            print("date:", expense["date"])
            print("category:", expense["category"])
            print("amount:", expense["amount"])
            print("description:", expense["description" ])
            print()
            

#ask for date or caregory or both, and show the matching expenses.
    def filter_expenses(self):
        print("press enter to skip any filter.")
        start_date = input("start_date (YYYY-MMM-DD): ")
        end_date = input("end_date (YYYY-MM-DD): ")
        category = input("category: ")

        matching_expenses = self.tracker.filter_expenses(
            start_date, end_date, category
        )
        self.print_expenses(matching_expenses)


#ask for a file name and save the current expenses to json.
    def save_to_json(self):
        file_name = input("enter file name: ")
        expenses = self.tracker.get_all_expenses()
        self.persister.save_json(expenses, file_name)
        print("expenses saved.")

#open json file and replace the current expense list.
    def open_from_json(self):
        file_name = input("enter file name: ")
        expenses = self.persister.load_json(file_name)
        self.tracker.set_expenses(expenses)
        print("expenses loaded")

#ask for a file name and export the current to csv.
    def export_to_csv(self):
        file_name = input("enter csv file name: ")
        expenses = self.tracker.get_all_expenses()
        self.persister.export_csv(expenses, file_name)
        print("expenses exported. ")
        