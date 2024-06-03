class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        else:
            print("Book is already borrowed ")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        else:
            print("Book not borrowed by this member")


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.borrow() and book not in self.borrowed_books:
            self.borrowed_books.append(book)
            return True
        

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            return True
        return print("Book not borrowed by this member")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)

    def register_member(self, member_id: str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)

    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            return member.borrow_book(book)
        elif member_id not in self.members:
            print("Member not found")
        else:
            print("Book not found")

    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            return member.return_book(book)
        return False

    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]
        return []