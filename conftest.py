import pytest

from main import BooksCollector


fantasy_book = 'Марсианин'
horror_book = 'Сияние'
detective_book = 'Рассказы о Шерлоке Холмсе'
child_book = 'Маленький принц'
comedy_book = 'Благие знамения'

@pytest.fixture(scope = 'function')
def books_collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope = 'function')
def prepare_books(books_collector):
    books_genre = [
        (fantasy_book, 'Фантастика'),
        (horror_book, 'Ужасы'),
        (detective_book, 'Детективы'),
        (child_book, 'Мультфильмы'),
        (comedy_book, 'Комедии')
    ]
    for book, genre in books_genre:
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
    return books_collector
