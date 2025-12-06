import manager_terminal
import provider_terminal
import generate_reports
from util import get_option

def main():

    do_main_menu = True

    while do_main_menu:
        print("Welcome to the Chocaholics Anonymous computer system!")
        print("Please choose an option:")
        print("1 - Run provider terminal")
        print("2 - Run manager terminal")
        print("3 - generate weekly reports")
        print("4 - Exit")

        option = get_option(4)

        if option == 1:
            provider_terminal.provider_terminal()
        elif option == 2:
            manager_terminal.manager_terminal()
        elif option == 3:
            generate_reports.generate_reports()
        else:
            do_main_menu = False



if __name__ == "__main__":
    main()
