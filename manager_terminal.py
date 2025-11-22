def manager_terminal():

    print("Welcome to the Chocaholics Anonymous Manager Terminal!")
    print("Please chose one of the following options:")
    print("1 - manage provider list")
    print("2 - manage service list")
    print("3 - manage member list")
    print("4 - exit")

    while True:
        try:
            option = int(input("Enter option: "))
            if 1 <= option <= 4:
                break
            else:
                print("Enter a valid option (1, 2, 3, or 4)")
        except ValueError:
            print("Enter a valid option (1, 2, 3, or 4)")