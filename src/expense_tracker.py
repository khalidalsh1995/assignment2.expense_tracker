"""this file stores expenses in a list and filters them."""


class ExpenseTracker:
#start with an empty expense list.
    def __init__(self):
        self.expenses = []

#add one expense to the list.
    def add_expense(self, date, category, amount, description):
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        self.expenses.append(expense)

#return the full expense list.
    def get_all_expenses(self):
        return self.expenses

#return only the expenses that match the filters.
    def filter_expenses(self, start_date, end_date, category):
        matching_expenses =[]

        for expense in self.expenses:
            if start_date and expense["date"] < start_date:
                continue

            if end_date and expense["date"] > end_date:
                continue

            if category and expense["category"].lower() != category.lower():
                continue

            matching_expenses.append(expense)

        return matching_expenses

#replace the current list with the new list
    def set_expenses(self, expenses):
        self.expenses = expenses