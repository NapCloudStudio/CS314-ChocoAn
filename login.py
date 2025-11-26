# login.py

def manager_login():
    VALID_USERNAME = "manager"
    VALID_PASSWORD = "admin123"

    print("=== Manager Login ===")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            print("Manager login successful!\n")
            return True
        else:
            print("Invalid login. Please try again.\n")


def provider_login():
    VALID_ID = "123456789"   # example provider ID

    print("=== Provider Login ===")

    while True:
        provider_id = input("Enter provider ID: ")

        if provider_id == VALID_ID:
            print("Provider login successful!\n")
            return True
        else:
            print("Invalid provider ID. Try again.\n")
