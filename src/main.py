"""this is the file you run to start Expense tracker."""

from cli_user_interface import CliUserInterface

#creates the user interface and starts the program.
def main():
    user_interface = CliUserInterface()
    user_interface.start_app()
    

if __name__ == "__main__":
    main()