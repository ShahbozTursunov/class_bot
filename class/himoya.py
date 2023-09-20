class My_school:
    address = "Yunusobod" # PUBLIC
    _Number = 999  # Protected
    __Name = "Maktab klassi" #Private
    
    
    def __init__(self, school_number, director, count_og_students, count_of_teachers) -> None:
        print("Init ishladi", self)
        self.school_number = school_number
        self.director = director
        self.count_of_students = count_og_students
        self.count_of_teachers = count_of_teachers
        
    # def __del__(self):
    #     print("Ochirildi")
    
    def get_info(self):
        print("Salom")
        
school = My_school(258, "FISH", 2222, 100)
school2 = My_school(258, "FISH", 2222, 100)
school2.school_number = 300
# print(school2.__Name)
print(school2._Number)


# class Mevalar:
#     def __init__(self, name, price, address) -> None:
#         self.name = name
#         self.__price = price
#         self._address = address
        
# fruit = Mevalar("Olma", 120000, "Yunusobod")
# print(fruit._address)
# print(fruit.__price)
# print(fruit.name)