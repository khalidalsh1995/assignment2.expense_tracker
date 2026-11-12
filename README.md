###Expense Tracker
this is a simple python program for tracking expenses. you can add expenses, view them and filter them. you can also save your expenses in json file, open them again later or export them to csv.

###Project files
-'main.py' -> starts the program.
-'cli_user_interface.py'-> show the menu and reads what you enter.
-'expense_tracker.py'-> keeps the expense list and filters it.
-'file_persister.py'-> reads and writes json files and expenses to csv.

###How to run

open git bash in the Hw2 folder and run:

from git bash
'
cd src
python main.py
'
if you are already in the 'src' folder, just run 'python main.py'.

###menu options
1-**add expense.** -> add one expense at a time. enter the date, category, amount and description.use 'YYYY-MM-DD'for the date.
2-**show all expenses.** -> see the current list. this includes expenses you added and expenses you opened from a saved file(json).
3-**filter expenses.** -> find expenses by date range, categpry or both. press enter to skip any field.
4-**save expenses to json** -> enter a file name like 'expenses.json'. if that file already exists, the current list replaces the list in file.
5-**open expenses from json** -> open a saved file. its expenses replace the current list. choose option 2 to see them.
6-**export expenses to CSV** -> enter a file name like 'expenses.csv'. each expense goes on its own row.
7-**exit** -> close the program. save your changes first if you want to keep them.

### How to keep your old expenses

if you saved two expenses yesterday and want to add one today, open your saved file first:

1.choose **5** and open your file like 'expenses.json'
2.choose **1** and add today's expense.
3.choose **2** and check that all three expenses are in the list.
4.choose **4** and save as 'expenses.json' again.

if you skip option 5 and save to the same file, the file will contain only the current list. your old expenses will be replaced. to keep the old file as it is, save with a diffrtent file name.