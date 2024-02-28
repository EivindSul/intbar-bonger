import unittest
from bong_generator import BongGenerator

class TestBongGenerator(unittest.TestCase):
    def test_get_control_number_adds_to_used_list(self):
        """Test that get_control_number adds number to used_control_numbers."""
        bong_generator = BongGenerator()
        control_number = bong_generator.get_control_number()
        self.assertTrue(len(control_number) == 5)
        self.assertIn(control_number, bong_generator.used_control_numbers)

    def test_get_control_number_is_5_long(self):
        """Test that get_control_number receives a string that is five long."""
        bong_generator = BongGenerator()
        control_number = bong_generator.get_control_number()
        self.assertTrue(len(control_number) == 5)

    def all_control_numbers_used(self):
        """Test that get_control_number raises an exception when all values between 00000 and 99999 are used up."""
        bong_generator = BongGenerator()
        for i in range(99999):
            bong_generator.used_control_numbers.append(str(i).zfill(5))
        # TODO: fiks dette
        control_number = bong_generator.get_control_number()
        self.assertTrue(len(control_number) == 5)

if __name__ == '__main__':
    unittest.main()

