class Library:

    def __init__(self):
        self.Shelves = []

    def PrintBooks(self):
        print("Listing books in library:")
        for s in self.Shelves:
            print("Shelf #" + str(s.Number))
            for b in s.Books:
                print("  Book: " + b.Title)


class Shelf:

    def __init__(self, number):
        self.Number = number
        self.Books = []


class Book:

    def __init__(self, title):
        self.Title = title
        self.CurrentShelf = None

    def Enshelf(self, shelf):
        if self.CurrentShelf is not None:
            self.Unshelf()
        shelf.Books.append(self)
        self.CurrentShelf = shelf

    def Unshelf(self):
        self.CurrentShelf.Books.remove(self)
        self.CurrentShelf = None

if __name__ == '__main__':
    MyLibrary = Library()
    Shelf1 = Shelf(1)
    Shelf2 = Shelf(2)
    Book1 = Book("The Joy of Cooking")
    Book2 = Book("The CodeFellows Guide to Life")
    Book3 = Book("C Primer - 4th Edition")

    MyLibrary.Shelves.append(Shelf1)
    MyLibrary.Shelves.append(Shelf2)

    Book1.Enshelf(Shelf1)
    Book2.Enshelf(Shelf1)
    Book3.Enshelf(Shelf1)
    Book3.Unshelf()
    Book3.Enshelf(Shelf2)

    MyLibrary.PrintBooks()
