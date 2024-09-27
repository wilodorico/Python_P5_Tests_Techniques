from typing import List


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return self.title

    def __repr__(self) -> str:
        return f"{self.title}"


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.borrowed_book_list: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Livre '{book.title}' ajouté avec succès !")
        print()

    def remove_book(self, book_title: str):
        for book in self.books:
            if book_title.lower() == book.title.lower():
                self.books.remove(book)
                print(f"Vous avez supprimer le livre {book_title}")
                print()
                return
        print(f"Livre {book_title} non trouvé")

    def borrow_book(self, book_title: str):
        for book in self.books:
            if book_title.lower() == book.title.lower():
                self.books.remove(book)
                self.borrowed_book_list.append(book)
                print(f"Vous avez emprunté le livre {book_title}")
                print()
                return

    def return_book(self, book_title: str):
        for book in self.borrowed_book_list:
            if book_title.lower() == book.title.lower():
                self.books.append(book)
                self.borrowed_book_list.remove(book)
                print(f"Vous avez rendu le livre {book_title}")
                print()
                return

    def available_books(self):
        if not self.books:
            print("Aucun livre disponible.")
        print(f"                      {len(self.books)} livre(s) disponible(s)")
        for book in self.books:
            print("===================================================================")
            print(f"Titre: {book.title}")
            print("===================================================================")
        print()

    def borrowed_books(self):
        if not self.borrowed_book_list:
            print("Aucun livre emprunté.")
        print(f"                 {len(self.borrowed_book_list)} livre(s) emprunté(s)")
        for book in self.borrowed_book_list:
            self.display_book_title(book_title=book.title)
        print()

    def display_book_title(self, book_title: str):
        print("=======================")
        print(f"Titre: {book_title}")
        print("=======================")


books = [
    Book("Apprendre à programmer avec Python 3", "Gérard Swinnen", 2012),
    Book("Domain-Driven Design", "Eric Evans", 2003),
    Book("Design patterns", "Eric Freeman", 2005),
    Book("Clean Code", "Robert C. Martin", 2008),
    Book("Test Driven Development", "Kent Beck", 2003),
    Book("The Pragmatic Programmer", "Andrew Hunt", 1999),
    Book("Refactoring", "Martin Fowler", 1999),
]

library = Library()

# Ajout des livres à la bibliothèque
for book in books:
    library.add_book(book)

library.available_books()

library.remove_book("Apprendre à programmer avec Python 3")

library.available_books()

# Emprunter un livre
library.borrow_book("Design patterns")
library.borrow_book("Refactoring")

library.borrowed_books()
library.available_books()


# Retouner un livre à la bibliothèque
library.return_book("Refactoring")
library.borrowed_books()
library.available_books()
