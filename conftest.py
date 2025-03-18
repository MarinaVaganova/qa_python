import pytest

from main import BooksCollector
from data import fantasy_book, horror_book, detective_book, child_book, comedy_book

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
