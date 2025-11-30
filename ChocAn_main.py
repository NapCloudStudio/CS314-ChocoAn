import manager_terminal
import provider_terminal
import generate_reports

def main():

    do_main_menu = True

    while do_main_menu == True
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

#asks the user to enter a number between 1 and count, and asks them to try again if they enter something else
def get_option(count):
    while True:
        try:
            option = int(input("Enter Option: "))
            if 1 <= option <= count:
                break
            else:
                print("Enter a valid option (", end = '')
                for i in range(1, count):
                    print(f"{i},", end = ' ')
                print(f"or {count}): ")

        except ValueError:
            print("Enter a valid option (", end = '')
            for i in range(1, count):
                    print(f"{i},", end = ' ')
            print(f"or {count}): ")
    return option





if __name__ == "__main__":
    main()