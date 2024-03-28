import enum

class BookGenre(enum.Enum):
    EMPTY = 0
    FANTASY = 1
    DETECTIVE = 2
    CLASSIC = 3


class Book:
    name = "Название"
    author = "Автор"
    pages = 0
    year_of_publishing = 0
    genre = BookGenre.EMPTY

    def __init__(
            self,
            name = "Название",
            author = "Автор",
            pages = 0,
            year_of_publishing = 0,
            genre = BookGenre.EMPTY
        ) -> None:
        self.name = name
        self.author = author
        self.pages = pages
        self.year_of_publishing = year_of_publishing
        self.genre = genre

    def get_author(self) -> str:
        return self.author

class Bookshelf:
    books = []

    def __init__(self) -> None:
        self.books = Bookshelf.books.copy()

    def add_book(book: Book) -> None:
        Bookshelf.books.append(book)
        print(f"Книга {book.name} была успешно добавлена")

    def add_obj_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Книга {book.name} была успешно добавлена")

    def remove_book(book: Book) -> None:
        Bookshelf.books.remove(book)
        print(f"Книга {book.name} была успешно удалена")

    def get_books_count() -> int:
        return len(Bookshelf.books)
    
    def print_catalog() -> None:
        for i, book in enumerate(Bookshelf.books, start = 1):
            print(f"{i}. {book.author}. {book.name}. {book.year_of_publishing}")

    def print_obj_catalog(self) -> None:
        for i, book in enumerate(self.books, start = 1):
            print(f"{i}. {book.author}. {book.name}. {book.year_of_publishing}")





captains_daughter = Book("Капитанская дочка", "А. С. Пушкин", 320, 1836, BookGenre.CLASSIC)
striped_hearse = Book("Полосатый катафалк", "Роcc Макдональд", 448, 2010, BookGenre.DETECTIVE)
lord_of_rings = Book("Властелин колец", "Дж. Р. Р. Толкин", 752, year_of_publishing = 1954, genre = BookGenre.FANTASY)
empty = Book()



Bookshelf.add_book(captains_daughter)
Bookshelf.add_book(striped_hearse)
Bookshelf.add_book(lord_of_rings)

Bookshelf.print_catalog()

print("==============================")

bookshelf = Bookshelf()
bookshelf.add_obj_book(empty)
bookshelf.print_obj_catalog()

Bookshelf.print_catalog()