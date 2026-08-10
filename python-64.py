#library - task

class library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def show_books(self):
         print("The books are : ")
         for book in self.books:
             print(book)
    
    def add_book(self,name):
        self.books.append(name)
        self.no_of_books +=1
    
    def num_books(self):
        print(f"total books : {self.no_of_books}")

a = library( )
a.add_book('fairytale')
a.add_book('disneyland')
a.show_books()
a.num_books()


