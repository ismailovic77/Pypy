# Simple concepts of inheritance and how they work 
# can add more about : 
    # multi-class inheritance 
    # Duck Typing in python and abstract classes (abstraction)
    # Two more concepts in OOP , (polymorphysme)
    # private feilds , static feilds (Encapsulation)

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("A new pet has been created")

    def speak(self):
        print("I don't know what to say")

    def show(self):
        print(f"I am {self.name} , and I have {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} , and I have {self.age} years old , and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

pet = Pet("Maxi", 5)
pet.show()
pet.speak()
print("*****************************")
dog = Dog("Alex", 10)
dog.show()
dog.speak()
print("*****************************")
cat = Cat("Supra", 10, "Black")
cat.show()
cat.speak()
