#User Interface Module

from ServiceBook import Service
from DomainBook import Book
import copy

class UI:

    def __init__(self, service):
        self.serviceBook = service
    
    def printMenu(self):
        print("")
        print("Menu for books:")
        print("     (1) to add a book to the list.")
        print("     (2) to show the list of books on the console.")
        print("     (3) to filter the list so that books titles strating with a given word are deleted to the list.")
        print("     (4) to undo the last operation.")
        print("     (0) to exit.")
    
    def addBook(self):
        print("")
        isbnInput = input("Give the isbn of the book: ")
        authorInput = input("Give the author of the book: ")
        titleInput = input("Give the title of the book: ")
        self.serviceBook.addBookToMainShelf(isbnInput, authorInput, titleInput)

    def showList(self):
        self.serviceBook.printList()

    def filterList(self):
        print("")
        givenWord = input("Give a word: ")
        self.serviceBook.filterList(givenWord)

    def undo(self):
        self.serviceBook.undoService()

    def generateRandomTitle(self):
        pass

    def run(self):

        self.serviceBook.addTenRandomBooks()
        self.serviceBook.initializeHistoryShelf()

        self.commands = {
            '1': self.addBook,
            '2': self.showList,
            '3': self.filterList,
            '4': self.undo,
            '9': self.generateRandomTitle
        }

        while True:
            self.printMenu()
            print("")
            command = input("Input command: ")
            if command == '0':
                return
            if command not in self.commands:
                print("")
                print("Not a valid command!")
            else:
                self.commands[command]()


service = Service()
ui = UI(service)
ui.run()