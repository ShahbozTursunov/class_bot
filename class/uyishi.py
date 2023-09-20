class School:
    def __init__(self, name, hisclass, ball, age, username):
        self.name = name
        self.hisclass = hisclass
        self.ball = ball
        self.age = age
        self.username = username
    
    def school_name(self):
        print(f"Oquvchining ismi {self.name}".title())
        
    def student_class(self):
        print(f"Uning sinifi {self.hisclass}".strip())
    
    def student_ball(self):
        print(f"Uning balli {self.ball}".upper())
        
    def student_age(self):
        print(f"Uning yoshi {self.age}".swapcase())
    
    def student_username(self):
        print(f"Uning familiyasi {self.username}".lower())
    def student_info(self):
        print(f"familiya {self.username} ismi {self.name}li oquvchi yoshi {self.age}, sinfi {self.hisclass}, bali {self.ball} shu.".capitalize())
        
        
# name = input("Iming nima: ")
# hiscall = input("sinfing nima: ")
# ball = input("Baling nima: ")
# age = input("Yoshing necchida: ")
# username = input("Familiyang nima: ")

# school = School(name, hiscall, ball, age, username)

school = School("Akbar", "7-B", 5, 12, "Millatulayeva")

school.school_name()
school.student_class()
school.student_ball()
school.student_age()
school.student_username()
school.student_info()