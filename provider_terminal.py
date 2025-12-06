import os
import datetime
import uuid
import json

from dao import DAO
from util import sha256, get_option
from data_classes import EFT, Provider, Member


def provider_terminal():
    global provider_id
    dao = DAO.chocan()
    print("ChocAn Provider Login")
    try:
        input_id = input("Provider ID: ")
        input_pw = input("Password: ")
        int_id = int(input_id)

        if sha256(input_pw) == dao.get_provider_password_hash(int_id) and \
                dao.get_provider_status(int_id) == Provider.STATUS_ACTIVE:
            print("Login successful!\n")
            provider_id = int_id
            menu()
        else:
            raise ValueError
    except ValueError:
        print("Invalid login.\n")
    except KeyboardInterrupt:
        exit(0)

def menu():
    do_provider_terminal = True

    while do_provider_terminal == True:
        print("Welcome to the Chocaholics Anonymous Provider Terminal!")
        print("Please chose one of the following options:")
        print("1 - validate member")
        print("2 - create service report")
        print("3 - display service directory")
        print("4 - exit")

        option = get_option(4)
        print()

        match option:
            case 1:
                validate_member()
            case 2:
                create_report()
            case 3:
                service_directory()
            case _:
                do_provider_terminal = False

def validate_member():
    data = DAO.chocan()

    while True:
        try:
            member = int(input("Enter Member ID: "))
            break
        except ValueError:
            print("Input must be an integer")

    status = data.get_member_status(member)

    if status == Member.STATUS_ACTIVE:
        print("membership validated")
    else:
        print("membership invalid")

def create_report():
    data = DAO.chocan()
    os.makedirs("eft/current", exist_ok=True)
    os.makedirs("provider_reports/current", exist_ok=True)
    os.makedirs("provider_reports/old", exist_ok=True)

    while True:
        try:
            member = int(input("Enter Member ID: "))
            break
        except ValueError:
            print("Input must be an integer")

    status = data.get_member_status(member)

    if status == Member.STATUS_ACTIVE:
        provider_name = data.get_provider_name(provider_id)
        if provider_name == None or data.get_provider_status(provider_id) != Provider.STATUS_ACTIVE:
            print("invalid provider id")
            return

        while True:
            try:
                service = int(input("Enter service code: "))
                break
            except ValueError:
                print("Input must be an integer")

        fee = data.get_service_fee(service)
        if fee == None:
            print("invalid service id")
            return

        comments = input("Enter up to 100 characters of comments: ")

        time = datetime.datetime.now()

        service_uuid = uuid.uuid4()
        filename = str(service_uuid) + ".txt"

        with open(f"provider_reports/current/{filename}", "wt") as filename:
            filename.write(f"Date and Time: {time}\n")
            filename.write(f"Provider number: {provider_id}\n")
            filename.write(f"Member number: {member}\n")
            filename.write(f"Service Code: {service}\n")
            filename.write(f"Comments: {comments}\n")

        print(f"service fee: {fee}")

        json_file = str(service_uuid) + ".json"
        with open(f"eft/current/{json_file}", "wt") as filename:
            filename.write(json.dumps({
                EFT.DATETIME: str(time),
                EFT.PROVIDER_ID: provider_id,
                EFT.PROVIDER_NAME: provider_name,
                EFT.FEE: fee
            }))

        print("created successfully\n")

    else:
        print("membership invalid")

def service_directory():
    data = DAO.chocan()
    data.print_services()
