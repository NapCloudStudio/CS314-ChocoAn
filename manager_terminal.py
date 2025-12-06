from dao import DAO
from util import get_option
from util import sha256


mgr_id = None

def manager_terminal():
    dao = DAO.chocan()
    print("\nLogin")
    input_id = input("User id: ")
    input_pw = input("Password: ")

    hash = dao.get_manager_password_hash(int(input_id))
    if hash == sha256(input_pw):
        print("Login successful!\n")
        mgr_id = input_id
        menu()
    else:
        print("Invalid login.")
        return

def menu():
    do_manager_terminal = True

    while do_manager_terminal:
        print("Welcome to the Chocaholics Anonymous Manager Terminal!")
        print("Please chose one of the following options:")
        print("1 - manage provider list")
        print("2 - manage service list")
        print("3 - manage member list")
        print("4 - exit")

        option = get_option(4)

        if option == 1:
           manage_providers()
        elif option == 2:
            manage_services()
        elif option == 3:
            manage_members()
        else:
            do_manager_terminal = False

def manage_providers():
    data = DAO.chocan()
    do_manage_providers = True

    while do_manage_providers == True:
        print("Provider list management:")
        print("Please chose one of the following options:")
        print("1 - add provider")
        print("2 - modify existing provider")
        print("3 - remove provider")
        print("4 - return to provider menu")

        option = get_option(4)
        
        if option == 1:
            name = input("Enter the provider's name: ")
            email = input("Enter the provider's email: ")

            #we might need to implement a hashing algorythm here, though for simplicitys sake we could just storte the passwords in plain text
            password = input("Enter the provider's password: ")
            street = input("Enter the provider's streed address: ")
            city = input("Enter the provider's city: ")
            state = input("Enter the provider's state: ")
            zipcode = input("Enter the provider's zip code: ")

            password_hash = sha256(password)

            address_id = data.create_address(street, city, state, zipcode)
            data.create_provider(name, password_hash, address_id, email, Provider.STATUS_ACTIVE)
        elif option == 2:
            while True:
                try:
                    to_modify = int(input("Enter the provider id of the provider record to be modified: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

                address = data.get_provider_addr_id(to_modify)

                if address == None:
                    print("Provider record not found")
                else:
                    name = input("Update the provider's name: ")
                    email = input("Update the provider's email:")
                    password = input("Update the providers password")
                    street = input("Update the provider's streed address: ")
                    city = input("Update the provider's city: ")
                    state = input("Update the provider's state: ")
                    zipcode = input("Update the provider's zip code: ")
                    status = input("Update the provider's status: ")

                    password_hash = sha256(password)

                    data.update_address(address, street, city, state, zipcode)
                    data.update_provider(to_modify, name, password_hash, email, status)

        elif option == 3:
            while True:
                try:
                    to_remove = int(input("Enter the provider id of the provider record to be removed: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

                removed = data.delete_provider(to_remove)

                if removed == True:
                    print("Provider record removed")
                else:
                    print("Provider record not found")
        else:
            do_manage_providers = False
        


def manage_services():
    data = DAO.chocan()
    do_manage_services = True

    while do_manage_services == True:
        print("Service list management:")
        print("Please chose one of the following options:")
        print("1 - add service")
        print("2 - remove service")
        print("3 - return to manager menu")

        option = get_option(3)

        if option == 1:
            name = input("Enter the service name: ")
            fee = input("Enter the service fee: ")

            data.create_service(name, fee)
        elif option == 2:
            while True:
                try:
                    to_remove = int(input("Enter the id of the service to be removed: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

            if data.delete_service() == True:
                print("service removed")
            else:
                print("service not found")
        
        else:
            do_manage_services = False

def manage_members():
    data = DAO.chocan()
    do_manage_members = True

    while do_manage_members == True:
        print("Member list management:")
        print("Please chose one of the following options:")
        print("1 - add member")
        print("2 - modify existing member")
        print("3 - remove member")
        print("4 - return to manager menu")

        option = get_option(4)

        if option == 1:
            name = input("Enter the member's name: ")
            street = input("Enter the member's streed address: ")
            city = input("Enter the member's city: ")
            state = input("Enter the member's state: ")
            zipcode = input("Enter the member's zip code: ")

            address_id = data.create_address(street, city, state, zipcode)
            data.create_member(name, address_id, Member.STATUS_ACTIVE)

        elif option == 2:
            while True:
                try:
                    to_modify = int(input("Enter the member id of the member record to be modified: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

            address = data.get_member_addr(to_modify)

            if address == None:
                print("Member not found")
            else:


                name = input("Update the member's name: ")
                street = input("Update the member's streed address: ")
                city = input("Update the member's city: ")
                state = input("Update the member's state: ")
                zipcode = input("Update the member's zip code: ")
                status = input("Update the member's status: ")

                data.update_address(address, street, city, state, zipcode)
                data.update_member(to_modify, name, status)

        elif option == 3:
            
            while True:
                try:
                    to_remove = int(input("Enter the member id of the member to be removed: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

            removed = data.delete_member(to_remove)

            if removed == True:
                print("Membership Terminated")
            else:
                print("Member not found")

        else:
            do_manage_members = False
