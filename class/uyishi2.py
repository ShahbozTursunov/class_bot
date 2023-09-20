# 1
class Book:
    def __init__(self, name, writer, janri, copy=1) -> None:
        self.name = name
        self.writer = writer
        self.janri = janri
        self.copy = copy
    def get_copy(self, name, writter, janri, copyre,):
        copyre += 1
        copy_n = [name, writter, janri, copyre].copy()
        print(copy_n)
    
    def return_copy(self, delete):
        del delete 
        if self.copy > 0:
            self.copy -= 1
    

     
name = input("Kitob nomi: ")
writter = input("Kitob yozuvchisi: ")
janri = input("Kitob janri: ")
copyre = 1
   
books = Book(name, writter, janri, copyre)



# 2
delete = books.get_copy(name, writter, janri, copyre)
books.return_copy(delete)