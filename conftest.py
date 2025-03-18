import pytest

from main import BooksCollector
from data import CHILD_BOOK, FANTASY_BOOK, COMEDY_BOOK, HORROR_BOOK, DETECTIVE_BOOK

@pytest.fixture(scope = 'function')
def books_collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope = 'function')
def prepare_books(books_collector):
    books_genre = [
        (FANTASY_BOOK, 'Фантастика'),
        (HORROR_BOOK, 'Ужасы'),
        (DETECTIVE_BOOK, 'Детективы'),
        (CHILD_BOOK, 'Мультфильмы'),
        (COMEDY_BOOK, 'Комедии')
    ]
    for book, genre in books_genre:
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
    return books_collector
