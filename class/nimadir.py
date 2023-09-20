class Car:
    def __init__(self, name, narx, rang):
        self.name = name
        self.price = narx
        self.color = rang
    
    def get_info(self):
        print(f"{self.name} li nomli moshinaning {self.color} rangliging narxi {self.price}")
        
    def get_color(self):
        print(f"{self.name} ning rangi {self.color}")
        
    def get_price(self):
        print(f"{self.name} ning narxi {self.price}")
    
    
    def get_name(self):
       print(f"Moshina nomi {self.name}")

car = Car(narx=200000, rang="qora", name="Audi")
car = Car("BMW", 55000, "kok")
# print(car.name)
car.get_info()
car.get_color()
car.get_price()
car.get_name()