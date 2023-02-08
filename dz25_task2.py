class Book:
    
    def __init__(self):
        self.name = input('Title of the book: ')
        self.yearPublication = int(input('Year of publication: '))
        self.publisher = input('Publishing house: ')
        self.genre = input('Genre: ')
        self.author = input('Author: ')
        self.bookPrice = int(input('Price: '))
        print('*'*40)

    def book_info(self):
        return f'Book - Title of the book: {self.name}, Year of publication: {self.yearPublication}, Publishing house: {self.publisher}, Genre: {self.genre}, Author: {self.author}, Price: {self.bookPrice}'

    def book_name(self):
        return f'Title of the book: {self.name}'

    def book_year(self):
        return f'Year of publication: {self.yearPublication}'

    def book_publisher(self):
        return f'Publishing house: {self.publisher}'

    def book_genre(self):
        return f'Genre: {self.genre}'

    def book_author(self):
        return f'Author: {self.author}'

    def book_price(self):
        return f'Price: {self.bookPrice}'

obj = Book()
print(obj.book_info())
print(obj.book_author())

