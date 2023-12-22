class Course:
    def __init__(self, code, name, credits, mandatory, instructor, time):
        self.code = code
        self.name = name
        self.credits = credits
        self.mandatory = mandatory
        self.instructor = instructor
        self.time = time

c1 = Course("CS101", "套裝軟體應用", 3, False, "李宗儒", "Fir 8:00 AM")
c2 = Course("ENG201", "微處理機應用實務, 3, Ture, "吳建中", "Wed 2:30 PM")

print("Course 1 Code:", c1.code)
print("Course 1 Name:", c1.name)
print("Course 1 Credits:", c1.credits)
print("Course 1 Mandatory:", c1.mandatory)
print("Course 1 Instructor:", c1.instructor)
print("Course 1 Time:", c1.time)

print("\nCourse 2 Code:", c2.code)
print("Course 2 Name:", c2.name)
print("Course 2 Credits:", c2.credits)
print("Course 2 Mandatory:", c2.mandatory)
print("Course 2 Instructor:", c2.instructor)
print("Course 2 Time:", c2.time)