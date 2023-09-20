class Kitob:
    def __init__(self, name, year, writter, page, price) -> None:
        self.name = name
        self.writter = writter
        self.year = year
        self.page = page
        self.price = price
        
    def get_name(self):
        print(f"Kitob nomi {self.name}")
        
    def get_year(self):
        print(f"{self.name} ning  yili {self.year}")
        
    def  get_writter(self):
        print(f"{self.name} ning  yozuvchisi {self.writter}")
        
    def  get_page(self):
        print(f"{self.name} {self.page} betdan  tashkil topgan")
        
    def  get_price(self):
        print(f"{self.name} ning narxi {self.price} so'm")
        
    
    def set_name(self, new_name):
        self.name = new_name
        
    def set_year(self, new_year):
        self.name = new_year
        
    def set_writter(self, new_writter):
        self.name = new_writter
        
    def set_page(self, new_page):
        self.name = new_page
        
    def set_price(self, new_price):
        self.name = new_price
        
        
book1 = Kitob("Garri Potter", 1999, "Julame", 198, 123000)
book2 = Kitob("Tungngi sarguzasht", 1899, "Mukamal", 250, 103000)
book3 = Kitob("Til boyligi", 1988, "Mexrinoz Teshaboyev", 458, 300000)
book4 = Kitob("Bolalik", 2000, "Ergashbekov", 500, 223000)
book5 = Kitob("Garri Potter 2", 1999, "Julame", 398, 523000)

book1.get_name()
book1.set_name("Garri Potter 3")

book2.get_writter()
book2.set_writter("Kamron Jabrrov")

book3.get_year()
book3.set_year(2005)

book4.get_page()
book4.set_page(234)

book5.get_price()
book5.set_price("1222200 so'm")