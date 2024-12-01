## Assignment 1: Design Your Own Class! 🏗️

# define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create a person object
person1 = Person("Alice", 25)

# Call the introduce method
person1.introduce()

# add an inheritance layer
class Student(Person):
    def __init__(self, name, age, grade_level, major):
        super().__init__(name, age)  # Inherit from the parent class
        self.grade_level = grade_level
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}.")

# Create a student object
student1 = Student("Alice", 16, 10, "Computer Science")

# Call methods from both the Person and Student classes
student1.introduce() 
student1.study()      


## Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def make_sound(self):
        pass  # Placeholder for subclasses

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Call the make_sound method on each animal
dog.make_sound()
cat.make_sound()
cow.make_sound()