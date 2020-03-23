#Domanain Module


class Book:

    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title
    
    def getIsbn(self):
        '''
        Function that gets the isbn of a book
        input:
        output: self.isbn - the isbn of a book
        '''
        return self.isbn
    
    def getAuthor(self):
        '''
        Function that gets the isbn of a book
        input:
        output: self.author - the author of a book
        '''
        return self.author
    
    def getTitle(self):
        '''
        Function that gets the isbn of a book
        input:
        output: self.title - the title of a book
        '''
        return self.title
    
    def setIsbn(self, newIsbn):
        '''
        Function that sets the isbn of a book
        input:
               newIsbn - a string
        output: -
        '''
        self.isbn = newIsbn
    
    def setAuthor(self, newAuthor):
        '''
        Function that sets the author of a book
        input:
               newAuthor - a string
        output: -
        '''
        self.author = newAuthor
    
    def setTitle(self, newTitle):
        '''
        Function that sets the title of a book
        input:
               newtitle - a string
        output:b -
        '''
        self.title = newTitle
    
    def addBookTo(self, shelf):
        '''
        Function that adds the book to a list
        input: shelf - a list
        '''
        shelf.append(self)
    
    
def testAddBookToShelf():
    shelf = []
    newBook = Book("9780743273565", "F. Scott Fitzgerald", "The Great Gatsby")
    newBook.addBookTo(shelf)
    assert shelf[0].isbn == "9780743273565"
    assert shelf[0].author == "F. Scott Fitzgerald"
    assert shelf[0].title == "The Great Gatsby"
    

testAddBookToShelf()
