import sqlite3
import os

def main():
    if os.path.exists("ChocAn.db"):
        os.remove("ChocAn.db")

    con = sqlite3.connect("ChocAn.db")

    cur = con.cursor()
    cur.execute("CREATE TABLE member(name, number, address, city, state, zipcode, status)")
    member_data = [
        ("James", 144435221, "Pyramid Valley Road", "Keswick", "IA", 50136, "valid"),
        ("Michael", 538597214, "2479 New York Avenue", "Dallas", "TX", 76031, "valid"),
        ("Robert", 396439244, "4530 Deercove Drive", "Cleburne", "TX", 76031, "valid"),
        ("John", 318888921, "4119 Roosevelt Street", "San Fransisco", "CA", 94143, "valid"),
        ("David", 925547066, "3009 Melm Street", "Lake City", "FL", 32055, "suspended"),
        ("William", 765634783, "805 Millbrook Road", "Naperville", "IL", 60540, "suspended"),
        ("Richard", 813541557, "1838 Longview Avenue", "New York", "NY", 10019, "valid"),
        ]
    cur.executemany("INSERT INTO member VALUES(?, ?, ?, ?, ?, ?, ?)", member_data)
    con.commit()

    cur.execute("CREATE TABLE provider(name, number, address, city, state, zipcode)")
    provider_data = [
        ("Dietary Clinic", 408562067, "3115 Hannah Street", "Andrews", "NC", 28901),
        ("Counseling Center", 357116153, "1110 Patterson Street", "Houston", "TX", 77002),
        ("Wellness Consultants", 423903697, "1640 Grant Street", "Plano", "TX", 75086),
        ]
    cur.executemany("INSERT INTO provider VALUES(?, ?, ?)", provider_data)
    con.commit()

    #price will be an integer represending dollar amount
    cur.execute("CREATE TABLE service(name, number, fee)")
    service_data = [
        ("Wellness Check", 445764, 50),
        ("Dietary Consultation", 325184, 75),
        ("Therapy Session", 819274, 80),
        ("Group Counselling", 321463, 40),
        ("Personal Trainer Session", 554292, 100),
        ]
    cur.executemany("INSERT INTO service VALUES(?, ?, ?, ?, ?)", service_data)
    con.commit



if __name__ == "__main__":
    main()
