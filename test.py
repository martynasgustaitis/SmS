import unittest
from unittest.mock import patch
import os
from io import StringIO

# Assuming the code above is in a file named 'user_manager.py'
from file_management import UserManager, UserFactory, RegularUser

class TestUserManager(unittest.TestCase):
    def setUp(self):
        # Setup temporary data files
        self.user_manager = UserManager()
        self.user_manager.data_file = 'test_users.txt'
        self.user_manager.history_file = 'test_operations_history.txt'
        self.user_manager.users = []
        self.clear_files()

    def tearDown(self):
        # Clean up the temporary data files
        self.clear_files()

    def clear_files(self):
        if os.path.exists(self.user_manager.data_file):
            os.remove(self.user_manager.data_file)
        if os.path.exists(self.user_manager.history_file):
            os.remove(self.user_manager.history_file)

    @patch('builtins.input', side_effect=['John Doe, 1990, Developer, 123-456-7890'])
    def test_add_new_user(self, mock_input):
        self.user_manager.add_new_user()
        self.assertEqual(len(self.user_manager.users), 1)
        self.assertEqual(self.user_manager.users[0].name, 'John Doe')

    @patch('builtins.input', side_effect=['John Doe'])
    def test_delete_user(self, mock_input):
        user = UserFactory.create_user("Regular", "John Doe", "1990", "Developer", "123-456-7890")
        self.user_manager.users.append(user)
        self.user_manager.delete_user()
        self.assertEqual(len(self.user_manager.users), 0)

    @patch('builtins.input', side_effect=['John Doe'])
    def test_find_info_by_name(self, mock_input):
        user = UserFactory.create_user("Regular", "John Doe", "1990", "Developer", "123-456-7890")
        self.user_manager.users.append(user)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.user_manager.find_info_by_name()
            self.assertIn('John Doe', fake_out.getvalue())

    def test_log_operation(self):
        self.user_manager.log_operation("Test operation")
        with open(self.user_manager.history_file, 'r') as file:
            operations = file.readlines()
        self.assertIn("Test operation\n", operations)

    def test_save_and_load_users(self):
        user = UserFactory.create_user("Regular", "John Doe", "1990", "Developer", "123-456-7890")
        self.user_manager.users.append(user)
        self.user_manager.save_users()
        self.user_manager.users = []
        self.user_manager.load_users()
        self.assertEqual(len(self.user_manager.users), 1)
        self.assertEqual(self.user_manager.users[0].name, 'John Doe')

    @patch('builtins.input', side_effect=['John Doe, 1990, Developer, 123-456-7890'])
    def test_add_new_user_logs_operation(self, mock_input):
        self.user_manager.add_new_user()
        with open(self.user_manager.history_file, 'r') as file:
            operations = file.readlines()
        self.assertIn("Added new user: John Doe\n", operations)

    @patch('builtins.input', side_effect=['John Doe'])
    def test_delete_user_logs_operation(self, mock_input):
        user = UserFactory.create_user("Regular", "John Doe", "1990", "Developer", "123-456-7890")
        self.user_manager.users.append(user)
        self.user_manager.delete_user()
        with open(self.user_manager.history_file, 'r') as file:
            operations = file.readlines()
        self.assertIn("Deleted user: John Doe\n", operations)

if __name__ == '__main__':
    unittest.main()
