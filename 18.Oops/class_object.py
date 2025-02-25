"""

A class is a blueprint

Student

roll_no

name

gender

standard

marks

"""

class Student:

    # Attributes

    roll_no = 0

    name = ""

    gender = ""

    standard = 0



s1 = Student()

s2 = Student()

s1.roll_no = 1

s1.name = "Anirudh"

s1.gender = "Male"

s1.standard = 12

print(s1.roll_no)

print(s1.name)

print(s1.gender)

print(s1.standard)

print("-------------")

print(s2.roll_no)

print(s2.name)

print(s2.gender)

print(s2.standard)


#--------------------------------

"""

A class is a blueprint

Student

roll_no

name

gender

standard

marks

"""



class Student:

    # Attributes

    roll_no = 0

    name = ""

    gender = ""

    standard = 0

    # Methods

    def display(self):

        print(f"Roll number = {self.roll_no}")

        print(f"Name = {self.name}")

        print(f"Gender = {self.gender}")

        print(f"Standard = {self.standard}")



s1 = Student()

s2 = Student()

s1.roll_no = 1

s1.name = "Anirudh"

s1.gender = "Male"

s1.standard = 12

s1.display()

print("---------")

s2.display()


####################################################

"""

A class is a blueprint

Student

roll_no

name

gender

standard

marks

"""



class Student:

    # Attributes

    # roll_no = 0

    # name = ""

    # gender = ""

    # standard = 0

    # Methods

    def display(self):

        print(f"Roll number = {self.roll_no}")

        print(f"Name = {self.name}")

        print(f"Gender = {self.gender}")

        print(f"Standard = {self.standard}")

    # def set_details(self):

    #     self.roll_no = int(input("Enter roll_no = "))

    #     self.name = input("Enter name = ")

    #     self.gender = input("Enter gender = ")

    #     self.standard = int(input("Enter standard = "))

    def set_details2(self, roll_no, name, gender, standard):

        self.roll_no = roll_no

        self.name = name

        self.gender = gender

        self.standard = standard



s1 = Student()

s1.set_details2(1, "Anirudh", "Male", 5)

s1.display()



#########################

"""

A class is a blueprint

Student

roll_no

name

gender

standard

marks

"""



class Student:

    # Attributes

    # roll_no = 0

    # name = ""

    # gender = ""

    # standard = 0

    # Special / Magic Methods

    def __init__(self):

        self.roll_no = int(input("Enter roll_no = "))

        self.name = input("Enter name = ")

        self.gender = input("Enter gender = ")

        self.standard = int(input("Enter standard = "))

    # Methods

    def display(self):

        print(f"Roll number = {self.roll_no}")

        print(f"Name = {self.name}")

        print(f"Gender = {self.gender}")

        print(f"Standard = {self.standard}")

    def set_details2(self, roll_no, name, gender, standard):

        self.roll_no = roll_no

        self.name = name

        self.gender = gender

        self.standard = standard



s1 = Student()

print("--------------")

# s1.set_details2(1, "Anirudh", "Male", 5)

s1.display()



##################################################

"""

A class is a blueprint

Student

roll_no

name

gender

standard

marks

"""



class Student:

    # Special / Magic Methods

    # Initializer

    def __init__(self, roll_no, name, gender, standard, school="SD Jain"):

        self.roll_no = roll_no

        self.name = name

        self.gender = gender

        self.standard = standard

        self.school = school

    # Methods

    def display(self):

        print(f"Roll number = {self.roll_no}")

        print(f"Name = {self.name}")

        print(f"Gender = {self.gender}")

        print(f"Standard = {self.standard}")



s1 = Student(1, "Anirudh", "Male", 7)

print("--------------")

# s1.set_details2(1, "Anirudh", "Male", 5)

s1.display()



#########################


"""

A class is a blueprint
Student
roll_no
name
gender
standard
marks

"""



class Student:
    # Special / Magic Methods
    # Initializer
    def __init__(self, roll_no, name, gender, standard, school="SD Jain"):
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.standard = standard
        self.school = school
    # Methods
    def display(self):
        print(f"Roll number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Standard = {self.standard}")
    def update_details(self, name=None, gender=None, standard=None):
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender
        if standard is not None:
            self.standard = standard



s1 = Student(1, "Anirudh", "Male", 7)
print("--------------")
# s1.set_details2(1, "Anirudh", "Male", 5)
s1.display()
s1.update_details(name="Sanjay")
s1.display()