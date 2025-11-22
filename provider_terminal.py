def provider_terminal():

    print("Welcome to the Chocaholics Anonymous Provider Terminal!")
    print("Please chose one of the following options:")
    print("1 - validate member")
    print("2 - create service report")
    print("3 - display service directory")
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


    #the corresponding function for each task will then be called