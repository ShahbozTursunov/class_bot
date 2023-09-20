# class Car:
#     def __init__(self, name, narx, rang) -> None:
#         self.name = name
#         self.narx = narx
#         self.rang = rang
    
#     def get_info(self):
#         print(f"Bu moshinaning nami {self.name}")
        
#     def get_color(self):
#         print(f"{self.name} ning rangi {self.rang}")
        
#     def get_price(self):
#         print(f"{self.name} ning narxi {self.narx}")
        
    
#     def set_price(self, new_price):
#         self.narx = new_price
        
#     def set_color(self, new_color):
#         self.rang = new_color
    
# car1 = Car("Matiz", 3500, "oq")
# car1.get_color()
# car1.set_color("qizil")
# car1.get_color()


# ________________________________________________________________________________________________________________________________


# 

# __________________________________________________________________________________________________-------


class Phone:
    def __init__(self, name, narx, year) -> None:
        self.name = name
        self._narx = narx
        self.__year = year
        
    def get_name(self):
        print(f"Moshina nomi{self.name}")
        
        
    def get_narx(self):
        print(f"Moshina nomi{self._narx}")
        
        
    def get_year(self):
        print(f"Moshina nomi{self.__year}")
        
        
    def get_info(self):
        print(f"{self.name} nomli moshina narxi {self._narx} rangi {self.__year}")
        
        
    def set_name(self, new_name):
        self.name = new_name
        
        
    def set_narx(self, new_narx):
        self._narx = new_narx
        
    def set_year(self, new_year):
        self.__year = new_year
        
        
telefon = Phone("Malibu", 12000000, 2002)
telefon.get_name()
telefon.get_narx()
telefon.get_year()
telefon.get_info()


telefon.set_name("Cobalt")
telefon.set_narx(1232000000)
telefon.set_name(1999)