import unittest
from util import validate_member_number, validate_provider_number

class TestUtil(unittest.TestCase):

    def test_validate_member_number_valid(self):
        self.assertTrue(validate_member_number("123456789"))

    def test_validate_member_number_invalid_length(self):
        self.assertFalse(validate_member_number("123"))

    def test_validate_verified_member_number_non_numeric(self):
        self.assertFalse(validate_member_number("ABC123456"))

    def test_validate_provider_number_valid(self):
        self.assertTrue(validate_provider_number("987654321"))

    def test_validate_provider_number_invalid(self):
        self.assertFalse(validate_provider_number("98X654321"))


if __name__ == "__main__":
    unittest.main()
