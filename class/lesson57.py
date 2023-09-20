class Mras_IT_School:
    rahbar = "Athamov Shasiyev"
    yonalishlar = ["starter", "fronted", "backend"]
    oquvchi = 2130


class Markaz:
    def __init__(self, number, students) -> None:
        self.number =  number
        self.students = students
        
cambridege = Markaz(34, 3458)

print(hasattr(cambridege, "number"))
# print(hasattr(cambridege, ))

# del cambridege.number
# print(cambridege.number)

# print(delattr(cambridege, "number"))
# print(cambridege.__dict__)
# print("number" in cambridege.__dict__)
# print("numbe" in cambridege.__dict__)

# print(cambridege.count)

# print(getattr(cambridege, "number"))
# print(getattr(cambridege, "count", "yoq"))

# cambridege.number = 55
# cambridege.students = 3445
# print(cambridege.__dict__)

setattr(cambridege, "number", "34")