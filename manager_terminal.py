from ChocAn_main import get_option
from dao import DAO
import util


mgr_id = None

def manager_terminal():
    dao = DAO.chocan()
    while True:
        print("\nLogin")
        input_id = input("User id: ")
        input_pw = input("Password: ")

        hash = dao.get_manager_password_hash(int(input_id))
        if hash == util.sha256(input_pw):
            print("Login successful!\n")
            mgr_id = input_id
            menu()
        else:
            print("Invalid login. Please try again.")

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

            address_id = data.create_address(street, city, state, zipcode)
            data.create_provider(name, password, address_id, email, "valid")
        elif option == 2:
            print("modify provider")
            #implement modify function on DAO
        elif option == 3:
            print("remove provider")
            #implement remove function
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
            #add remove service function for DAO
            print("remove service")
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

            address_id = data.create_address(street, city, state, zip)
            data.create_member(name, address_id, "valid")

        elif option == 2:
            while True:
                try:
                    to_remove = int(input("Enter the member id of the member record to be modified: "))
                    break
                except(ValueError):
                    print("Input must be an integer")

            name = input("Update the member's name: ")
            street = input("Update the member's streed address: ")
            city = input("Update the member's city: ")
            state = input("Update the member's state: ")
            zipcode = input("Update the member's zip code: ")

            #need to modify the database update function to support addresses

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
