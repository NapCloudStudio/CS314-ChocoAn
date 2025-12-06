import hashlib

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

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
