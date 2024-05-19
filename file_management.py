from abc import ABC, abstractmethod
import os

# Abstract base class for User
class User(ABC):
    def __init__(self, name, birth_year, position, phone_number):
        self.name = name
        self.birth_year = birth_year
        self.position = position
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Birth Year: {self.birth_year}, Position: {self.position}, Phone Number: {self.phone_number}"

    @abstractmethod
    def update_info(self, **kwargs):
        pass

# Concrete implementation of User
class RegularUser(User):
    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

# Factory Method pattern for creating users
class UserFactory:
    @staticmethod
    def create_user(user_type, name, birth_year, position, phone_number):
        if user_type == "Regular":
            return RegularUser(name, birth_year, position, phone_number)
        else:
            raise ValueError(f"Unknown user type: {user_type}")

# Singleton pattern for managing users
class UserManager:
    _instance = None
    data_file = 'users.txt'
    history_file = 'operations_history.txt'

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = []
            cls._instance.load_users()
        return cls._instance

    def add_new_user(self):
        print("To add new user write It’s: name, birth year, position, phone number")
        user_data = input().split(', ')
        user = UserFactory.create_user("Regular", user_data[0], user_data[1], user_data[2], user_data[3])
        self.users.append(user)
        self.save_users()
        self.log_operation(f"Added new user: {user.name}")
        print(f"User {user.name} added successfully.")

    def add_info_to_user(self):
        print("To add info to user write It’s: name")
        name = input()
        user = self.find_user_by_name(name)
        if user:
            missing_fields = [key for key, value in user.__dict__.items() if not value]
            if missing_fields:
                print(f"The following information is missing for {name}: {', '.join(missing_fields)}")
                new_info = {field: input(f"Please enter {field}: ") for field in missing_fields}
                user.update_info(**new_info)
                self.save_users()
                self.log_operation(f"Updated info for user: {user.name}")
                print(f"Information for {name} updated successfully.")
            else:
                print(f"No information is missing for {name}.")
        else:
            print(f"No user found with the name {name}.")

    def delete_user(self):
        print("To delete user write It’s: name")
        name = input()
        self.users = [user for user in self.users if user.name != name]
        self.save_users()
        self.log_operation(f"Deleted user: {name}")
        print(f"Info of {name} was deleted.")

    def find_info_by_name(self):
        print("To find user's info write It’s: name")
        name = input()
        user = self.find_user_by_name(name)
        if user:
            print(user)
            self.log_operation(f"Found info for user: {user.name}")
        else:
            print(f"No user found with the name {name}.")

    def find_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def save_users(self):
        with open(self.data_file, 'w') as file:
            for user in self.users:
                file.write(f"{user.name},{user.birth_year},{user.position},{user.phone_number}\n")

    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                for line in file:
                    name, birth_year, position, phone_number = line.strip().split(',')
                    user = UserFactory.create_user("Regular", name, birth_year, position, phone_number)
                    self.users.append(user)

    def log_operation(self, operation):
        with open(self.history_file, 'a') as file:
            file.write(f"{operation}\n")

    def read_operation_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                for line in file:
                    print(line.strip())

def main():
    user_manager = UserManager()  # Singleton instance of UserManager
    while True:
        print("\nChoose an option:")
        print("1. Add new user")
        print("2. Add info to user")
        print("3. Delete user")
        print("4. Find info by the name")
        print("5. Exit")
        
        choice = input()
        if choice == '1':
            user_manager.add_new_user()
        elif choice == '2':
            user_manager.add_info_to_user()
        elif choice == '3':
            user_manager.delete_user()
        elif choice == '4':
            user_manager.find_info_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
