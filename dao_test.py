import os
from dao import DAO
from data_classes import *


database_path = "test.db"
if os.path.exists(database_path):
    os.remove(database_path)

dao = DAO(database_path)


def create_tables():
    dao.create_tables()

def add_test_data_manager():
    dao.create_manager("admin", "admin")
    dao.create_manager("John Manager", "password123")

def add_test_data_member():
    ma1 = dao.create_address("Pyramid Valley Road", "Keswick", "IA", "50136")
    dao.create_member("James", ma1, Member.STATUS_ACTIVE)
    ma2 = dao.create_address("2479 New York Avenue", "Dallas", "TX", "76031")
    dao.create_member("Michael", ma2, Member.STATUS_ACTIVE)
    ma3 = dao.create_address("4530 Deercove Drive", "Cleburne", "TX", "76031")
    dao.create_member("Robert", ma3, Member.STATUS_ACTIVE)
    ma4 = dao.create_address("4119 Roosevelt Street", "San Fransisco", "CA", "94143")
    dao.create_member("John", ma4, Member.STATUS_ACTIVE)
    ma5 = dao.create_address("3009 Melm Street", "Lake City", "FL", "32055")
    dao.create_member("David", ma5, Member.STATUS_INACTIVE)
    ma6 = dao.create_address("805 Millbrook Road", "Naperville", "IL", "60540")
    dao.create_member("William", ma6, Member.STATUS_INACTIVE)
    ma7 = dao.create_address("1838 Longview Avenue", "New York", "NY", "10019")
    dao.create_member("Richard", ma7, Member.STATUS_ACTIVE)

def add_test_data_provider():
    pa1 = dao.create_address("3115 Hannah Street", "Andrews", "NC", "28901")
    dao.create_provider("Dietary Clinic", "123456", pa1, "dietaryclinic@example.com", Provider.STATUS_ACTIVE)
    pa2 = dao.create_address("1110 Patterson Street", "Houston", "TX", "77002")
    dao.create_provider("Counseling Center", "cchouston", pa2, "cchouston@example.com", Provider.STATUS_ACTIVE)
    pa3 = dao.create_address("1640 Grant Street", "Plano", "TX", "75086")
    dao.create_provider("Wellness Consultants", "correcthorsebatterystaple", pa3, "wellness@example.com", Provider.STATUS_ACTIVE)

def add_test_data_service():
    dao.create_service("Wellness Check", 50)
    dao.create_service("Dietary Consultation", 75)
    dao.create_service("Therapy Session", 80)
    dao.create_service("Group Counselling", 40)
    dao.create_service("Personal Trainer Session", 100)

def get_manager_pw_hashes():
    print(f"manager 1: '{dao.get_manager_password_hash(1)}'")
    print(f"manager 2: '{dao.get_manager_password_hash(2)}'")

def get_provider_pw_hashes():
    print(f"provider 1: '{dao.get_provider_password_hash(1)}'")
    print(f"provider 2: '{dao.get_provider_password_hash(2)}'")

def get_member_status():
    print(f"member 1: {dao.get_member_status(1)}")
    print(f"member 2: {dao.get_member_status(2)}")
    print(f"member 3: {dao.get_member_status(3)}")
    print(f"member 4: {dao.get_member_status(4)}")
    print(f"member 5: {dao.get_member_status(5)}")

def update_addr():
    dao.update_address(1, zip="asdf", city="zxcv")
    dao.update_address(2, state="test", street="text")
    dao.update_address(3)
    dao.update_address(4, street="123 STREET BLVD", city="TOWNSVILLE", state="SOMEWHERE", zip="abc123")

def _delete_p(id: int):
    p = dao.get_provider_status(id)
    assert p != Provider.STATUS_INACTIVE, "member already inactive"
    dao.delete_provider(id)
    p = dao.get_provider_status(id)
    assert p == Provider.STATUS_INACTIVE, "member should be inactive"
def delete_p():
    _delete_p(1)
    _delete_p(2)
    _delete_p(3)
    print("delete provider passed")

def _delete_m(id: int):
    m = dao.get_member_status(id)
    assert m != Member.STATUS_INACTIVE, "member already inactive"
    dao.delete_member(id)
    m = dao.get_member_status(id)
    assert m == Member.STATUS_INACTIVE, "member should be inactive"
def delete_m():
    _delete_m(1)
    _delete_m(2)
    _delete_m(3)
    print("delete member passed")

if __name__ == "__main__":
    create_tables()
    add_test_data_manager()
    add_test_data_provider()
    add_test_data_member()
    add_test_data_service()

    get_manager_pw_hashes()
    get_provider_pw_hashes()
    get_member_status()

    update_addr()

    delete_p()
    delete_m()
