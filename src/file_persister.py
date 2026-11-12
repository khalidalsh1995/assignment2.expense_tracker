"""this file saves, reads json files and exports expenses csv."""


import csv
import json

class FilePersister:
#save the expense list to json file.
    def save_json(self, expenses, file_name):
        with open(file_name, "w") as json_file:
            json.dump(expenses, json_file, indent=4)

#read the expense list from a json file and return it.
    def load_json(self, file_name):
        with open(file_name, "r") as json_file:
            expenses = json.load(json_file)

        return expenses

#write the expenses to a csv file, one expense per row.
    def export_csv(self, expenses, file_name):
        columns =["date", "category", "amount", "description"]

        with open(file_name, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()

            for expense in expenses:
                writer.writerow(expense)