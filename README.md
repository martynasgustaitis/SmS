# REPORT
Introduction:
My project made simple school management system (SmS) which allows you to upload persons basic information, change it, find it, and delete it.
To run program, you have to open file in vs code, run it, it will display meniu, from which you choose aplication you want to use.
All of the functional requirements are explained below

1.	Singleton Pattern:
•	Why it is suitable: The Singleton Pattern is used to ensure that only one instance of a class is created and provides a global point of access to that instance. This is particularly useful in scenarios where a single resource, such as a configuration manager or in our case, a user manager, is required to coordinate actions across the system.
•	How it works: The Singleton Pattern is implemented in the UserManager class. The __new__ method is overridden to ensure that only one instance of UserManager is created. A class attribute _instance is used to store this single instance. When UserManager is instantiated, it checks if _instance is None. If it is, a new instance is created and assigned to _instance. Otherwise, the existing instance is returned.
•	Why it is most suitable: For user management, it is critical to have a single point of control to avoid conflicts and ensure consistent state management. The Singleton Pattern guarantees that there is only one UserManager handling all user-related operations, making the system simpler and more reliable.
2.	Factory Method Pattern:
•	Why it is suitable: The Factory Method Pattern is used to define an interface for creating an object but allows subclasses to alter the type of objects that will be created. This pattern provides a flexible and reusable way to instantiate objects, especially when the exact type of object to create is not known until runtime.
•	How it works: The Factory Method Pattern is implemented in the UserFactory class. The create_user method takes a user_type and user details as arguments and returns an instance of the appropriate user class. Currently, it only supports creating RegularUser objects, but it can be easily extended to support additional user types in the future.
•	Why it is most suitable: In scenarios where we may need to support different types of users with varying behaviors and characteristics, the Factory Method Pattern provides a flexible approach to object creation. This makes the system easily extendable and maintainable, allowing for new user types to be added with minimal changes to the existing codebase.

OOP pilars
*Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is typically achieved through method overriding, where subclasses provide specific implementations of methods declared in their superclasses.
In my code, polymorphism is exhibited by the update_info method. Different user types (e.g., RegularUser) can implement their own version of this method.
# Polymorphism snippet
user = RegularUser("Alice", 1990, "Developer", "123456789")
user.update_info(phone_number="987654321")


*Abstraction
Abstraction involves creating simple, easy-to-use interfaces for more complex underlying code. Abstract classes and methods provide a template for other classes to implement.
User class is an abstract class, and the update_info method is an abstract method.This ensures that any subclass of User must implement the update_info method.
# Abstraction snippet
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def update_info(self, **kwargs):
        pass


*Inheritance
Inheritance allows a class to inherit attributes and methods from another class. In my code, RegularUser inherits from User.
# Inheritance snippet
class RegularUser(User):
    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


# RegularUser inherits all attributes and methods from User

*encapsulation
Encapsulation is the bundling of data and methods that operate on that data within one unit, often a class, and restricting access to some of the object's components.
In my code, user data is encapsulated within the User class. The attributes are protected from direct access from outside the class, and interaction is done through methods.
# Encapsulation snippet
class User(ABC):
    def __init__(self, name, birth_year, position, phone_number):
        self.name = name
        self.birth_year = birth_year
        self.position = position
        self.phone_number = phone_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
#RESULTS
Biggest challenge was to understand what was needed to do and how should it look. One of the biggest issues i've had was linking github with vs code and adding txt file, we didn't have any practice on that.

#CONCLUSION
Simple management system was made, It runs great, has lots of potencial, like adding everyones schedules and make it show by the name of person.
Adding grading, and attendance to system would make It more suitable to use by schools.
