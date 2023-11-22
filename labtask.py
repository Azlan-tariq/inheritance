# FileNameOFyourchoice.py
print("single inheritance")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.\n")

# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Using methods from the base class
my_dog.speak()

# Using methods from the derived class
my_dog.bark()
 
#multilevel task

print("multilevel inheritance \n")
# FileNameOFyourchoice.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} gives birth to live young.")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name} barks.")

# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Using methods from the base class
my_dog.speak()

# Using methods from the intermediate class
my_dog.give_birth()

# Using methods from the derived class
my_dog.bark()


print("hierarchical inheritance\n")

# FileNameOFyourchoice.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.\n")

# Creating instances of the derived classes
my_cat = Cat("Whiskers")
my_dog = Dog("Buddy")

# Using methods from the base class
my_cat.speak()
my_dog.speak()

# Using methods from the derived classes
my_cat.meow()
my_dog.bark()


print("multiple inheritance")

# FileNameOFyourchoice.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Salary: ${self.salary}")

class Student:
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")

class EmployeeAndStudent(Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        # Calling constructors of both base classes
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        Student.__init__(self, student_id, grade)

# Creating an instance of the derived class
employee_and_student = EmployeeAndStudent("John", 25, "E123", 50000, "S456", "A")

# Using methods from the base classes
employee_and_student.display_info()  # This will call the display_info method from the Employee class



