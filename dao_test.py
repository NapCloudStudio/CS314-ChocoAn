import hashlib
from dao import DAO


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def create_tables():
    DAO().create_tables()

def add_test_data_manager():
    DAO().create_manager("admin", sha256("admin"))
    DAO().create_manager("John Manager", sha256("password123"))

def add_test_data_member():
    dao = DAO()
    ma1 = dao.create_address("Pyramid Valley Road", "Keswick", "IA", "50136")
    dao.create_member("James", ma1, "active")
    ma2 = dao.create_address("2479 New York Avenue", "Dallas", "TX", "76031")
    dao.create_member("Michael", ma2, "active")
    ma3 = dao.create_address("4530 Deercove Drive", "Cleburne", "TX", "76031")
    dao.create_member("Robert", ma3, "active")
    ma4 = dao.create_address("4119 Roosevelt Street", "San Fransisco", "CA", "94143")
    dao.create_member("John", ma4, "active")
    ma5 = dao.create_address("3009 Melm Street", "Lake City", "FL", "32055")
    dao.create_member("David", ma5, "inactive")
    ma6 = dao.create_address("805 Millbrook Road", "Naperville", "IL", "60540")
    dao.create_member("William", ma6, "inactive")
    ma7 = dao.create_address("1838 Longview Avenue", "New York", "NY", "10019")
    dao.create_member("Richard", ma7, "active")

def add_test_data_provider():
    dao = DAO()
    pa1 = dao.create_address("3115 Hannah Street", "Andrews", "NC", "28901")
    dao.create_provider("Dietary Clinic", sha256("123456"), pa1, "dietaryclinic@example.com", "active")
    pa2 = dao.create_address("1110 Patterson Street", "Houston", "TX", "77002")
    dao.create_provider("Counseling Center", sha256("cchouston"), pa2, "cchouston@example.com", "active")
    pa3 = dao.create_address("1640 Grant Street", "Plano", "TX", "75086")
    dao.create_provider("Wellness Consultants", sha256("correcthorsebatterystaple"), pa3, "wellness@example.com", "active")

def add_test_data_service():
    DAO().create_service("Wellness Check", 50)
    DAO().create_service("Dietary Consultation", 75)
    DAO().create_service("Therapy Session", 80)
    DAO().create_service("Group Counselling", 40)
    DAO().create_service("Personal Trainer Session", 100)

def get_pw_hashes():
    m_id = 1
    res = DAO().get_manager_password_hash(m_id)
    print(f"manager: '{res}'")

    p_id = 1
    res = DAO().get_provider_password_hash(p_id)
    print(f"provider: '{res}'")

def get_member_status():
    print("1: " + DAO().get_member_status(1))
    print("2: " + DAO().get_member_status(2))
    print("3: " + DAO().get_member_status(3))
    print("4: " + DAO().get_member_status(4))
    print("5: " + DAO().get_member_status(5))

if __name__ == "__main__":
    create_tables()
    add_test_data_manager()
    add_test_data_provider()
    add_test_data_member()
    add_test_data_service()
    get_pw_hashes()
    get_member_status()
