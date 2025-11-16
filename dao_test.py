from dao import DAO

if __name__ == "__main__":
    dao = DAO()
    dao.create_tables()

    dao.create_manager("admin", "")
    dao.create_manager("John Manager", "")

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

    pa1 = dao.create_address("3115 Hannah Street", "Andrews", "NC", "28901")
    dao.create_provider("Dietary Clinic", "", pa1, "dietaryclinic@example.com", "active")
    pa2 = dao.create_address("1110 Patterson Street", "Houston", "TX", "77002")
    dao.create_provider("Counseling Center", "", pa2, "cchouston@example.com", "active")
    pa3 = dao.create_address("1640 Grant Street", "Plano", "TX", "75086")
    dao.create_provider("Wellness Consultants", "", pa3, "wellness@example.com", "active")

    dao.create_service("Wellness Check", 50),
    dao.create_service("Dietary Consultation", 75),
    dao.create_service("Therapy Session", 80),
    dao.create_service("Group Counselling", 40),
    dao.create_service("Personal Trainer Session", 100),
