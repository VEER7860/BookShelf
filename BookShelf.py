from tkinter import *
root = Tk()
root.title("BookShelf")
root.geometry("500x500")


class BookShelf:
 def __init__(self,book_name,book_author,book_price,years):
        self.book_name = book_name
        self.book_author = book_author
        self.book_price = book_price
        self.years_since_book_published = years
       
        
 def add_bookshelf(self): 
        print("Book Name: "+self.book_name)
        print("Book Author:"+self.book_author)
        print("Book Price:"+str(self.book_price))
        print("Book was published in  "+self.years_since_book_published)
        print("Book Added")
        
bookshelf1 = BookShelf("Harry Potter", "J.K. Rowling", 1928, "23 years ago")
bookshelf1.add_bookshelf()

bookshellf2= BookShelf("Diary of a Wimpy Kid","Jeff Kinney ",700,"3 year ago")
bookshellf2.add_bookshelf()
root.mainloop()