import manager_terminal
import provider_terminal
import generate_reports

def main():
    print("Welcome to the Chocaholics Anonymous computer system!")
    print("Please choose an option:")
    print("1 - Run provider terminal")
    print("2 - Run manager terminal")
    print("3 - generate weekly reports")

    while True:
        try:
            option = int(input("Enter option: "))
            if 1 <= option <= 3:
                break
            else:
                print("Enter a valid option (1, 2, or 3)")
        except ValueError:
            print("Enter a valid option (1, 2, or 3)")

    if option == 1:
        provider_terminal.provider_terminal()
    elif option == 2:
        manager_terminal.manager_terminal()
    else:
        generate_reports.generate_reports()




if __name__ == "__main__":
    main()