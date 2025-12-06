import unittest
from login import Login
from dao import DAO

class FakeDAO(DAO):
    def __init__(self):
        self.users = {
            "provider1": ("123456789", "provider"),
            "manager1": ("987654321", "manager"),
        }

    def validate_login(self, username, number):
        if username in self.users and self.users[username][0] == number:
            return self.users[username][1]
        return None


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.dao = FakeDAO()
        self.login = Login(self.dao)

    def test_valid_provider_login(self):
        role = self.login.login("provider1", "123456789")
        self.assertEqual(role, "provider")

    def test_valid_manager_login(self):
        role = self.login.login("manager1", "987654321")
        self.assertEqual(role, "manager")

    def test_login_invalid_username(self):
        role = self.login.login("invalid", "000000000")
        self.assertIsNone(role)

    def test_login_wrong_number(self):
        role = self.login.login("provider1", "111111111")
        self.assertIsNone(role)


if __name__ == "__main__":
    unittest.main()
