# class Shaxs:
#     def __init__(self, fullname, age, address, phone) -> None:
#         self.fullname = fullname
#         self.age = age
#         self.address = address
#         self.phone = phone
        
#     def get_age(self):
#         return f"{self.fullname} {self.age} yoshda"
    
#     def set_age(self, new_age):
#         self.age = new_age
        
# doni = Shaxs("Doniyor Usmonov", 67, "Mars", "+734394826534")
# print(doni.get_age())
# doni.set_age(89)
# print(doni.get_age())

# class Talaba(Shaxs):
#     def __init__(self, fullname, age, address, phone) -> None:
#         super().__init__(fullname, age, address, phone)
        
# tolib = Talaba("Kamron Jabborov", 14, "Yunusobod", "9998877")
# print(tolib.address)
# print(tolib.get_age())

class Shaxs:
    def __init__(self, fullname, age, address, phone) -> None:
        self.fullname = fullname
        self.age = age
        self.address = address
        self.phone = phone
        
    def get_age(self):
        return f"{self.fullname} {self.age} yoshda"
    
    def set_age(self, new_age):
        self.age = new_age
        
doni = Shaxs("Doniyor Usmonov", 67, "Mars", "+734394826534")
print(doni.get_age())
doni.set_age(89)
print(doni.get_age())

class Talaba(Shaxs):
    def __init__(self, fullname, age, address, phone, univ, course) -> None:
        super().__init__(fullname, age, address, phone)
        self.univertsity = univ
        self.course = course
        
    def get_univ(self):
        return f"{self.fullname} {self.univertsity} da o'qiydi"

        
tolib = Talaba("Kamron Jabborov", 14, "Yunusobod", "9998877", "MARS IT", 3)
print(tolib.address)
print(tolib.get_age())
print(tolib.get_univ())