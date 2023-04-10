# 1

def count_vowels(text):
    if not isinstance(text, str):
        return 42

    count = 0

    for char in text:
        if char in "AEIOUaeiou":
            count += 1
    return count



x = input("Enter a phrase: ")
print(count_vowels(x))

# 2


def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0

    count2 = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            count2 = count2 + 1
    return count2



print("Hamming distance", hamming("b,c,c", "a,b,c,d"))


#3

class Vehicle:

    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color <{self.color}>, Fuel Type <{self.fuel_type}>, Doors <{self.doors}>"


car1 = Car("red", "diesel", "2")
print(car1.color)
print(car1.doors)
print(car1.__str__())


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color <{self.color}>, Fuel Type <{self.fuel_type}>, Passengers <{self.passengers}>"


bus1 = Bus("yellow", "diesel", "60")
print(bus1.__str__())

# 4


class Book:

     def __init__(self, name, author):
        self.name = name
        self.author = author

     def __str__(self):
         return f"{self.name}, {self.author}"



book1 = Book("Hamlet", "Shakespeare")
print(book1)

# 5

class BookShelf:

    def __init__(self):
        self.books = []

    #def add_book_list(self, books):
        #for book in books:
            #if isinstance()

    #def books_by_author(self, author):


    #def get_books(self):

    #def clear_shelf(self,):


#books = ["Hamlet", "Romeo and Juliet", ]
#author = [""]
#book1 = BookShelf["Hamlet", "Romeo und Juliet"]
#print(book1)