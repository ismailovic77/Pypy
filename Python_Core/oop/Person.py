# define here a person method , with some static attributes and class methods , with the cls and the decorator @classmethod
# static method is just like a class method , not related to the instance basically , but it does not change anything inside
# the class not like the classmethod that usually changes the values of static attributes

class Person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.add_person()
        print(f"A person {self.name} was created")
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people
    
    @staticmethod
    def pr_info():
        desc = """
this is static method that print general description about human being , no relation to the actual instance
            """
        print(desc)
            

p1 = Person("Ismail")
print(Person.get_number_of_people()) 
p2 = Person("Taha")
print(Person.get_number_of_people())    
p3 = Person("Hiba")
print(Person.get_number_of_people())    
#**********
print(Person.number_of_people)

# static methods 
Person.pr_info()
