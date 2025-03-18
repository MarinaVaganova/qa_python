import pytest

from data import CHILD_BOOK, FANTASY_BOOK, COMEDY_BOOK, HORROR_BOOK, DETECTIVE_BOOK


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Проверка добавления 2-х книг с одинаковым названием
    def test_add_new_book_add_duplicate_book(self, books_collector):
        books_collector.add_new_book(CHILD_BOOK)
        books_collector.add_new_book(CHILD_BOOK)
        assert len(books_collector.get_books_genre()) == 1

    # Проверка добавления книги с названием более 40 символов
    def test_add_new_book_add_book_more_40_symbols(self, books_collector):
        books_collector.add_new_book('Сияние Сияние Сияние Сияние Сияниееееееее')
        assert len(books_collector.get_books_genre()) == 0

    # Проверка, что если жанр не входит в список genre, он не устанавливается
    def test_set_book_genre_invalid_genre(self, books_collector, prepare_books):
        books_collector.set_book_genre(FANTASY_BOOK, 'Биография')
        assert books_collector.books_genre[FANTASY_BOOK] != 'Биография'

    # Проверка вывода книги определенного жанра
    def test_get_books_with_specific_genre_book_get_list_genre(self, books_collector, prepare_books):
        genre = 'Фантастика'
        assert books_collector.get_books_with_specific_genre(genre) == [FANTASY_BOOK]

    # Проверка вывода пустого словаря, если в коллекции нет книг
    def test_get_books_genre_empty(self, books_collector):
        assert books_collector.get_books_genre() == {}

    # Проверка корректного вывода словаря для разных книг и жанров
    @pytest.mark.parametrize('book, genre', [('Марсианин', 'Фантастика'),('Сияние','Ужасы'),('Маленький принц','Мультфильмы')])
    def test_get_books_genre_different_books_and_genres(self, books_collector, book, genre):
        books_collector.add_new_book(book)
        books_collector.set_book_genre(book, genre)
        assert books_collector.get_books_genre() == {book: genre}

    # Проверка списка книг, подходящих детям
    def test_get_books_for_children_three_books_get_list_books(self, books_collector, prepare_books):
        assert books_collector.get_books_for_children() == [FANTASY_BOOK, CHILD_BOOK, COMEDY_BOOK]

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_book_success(self, books_collector, prepare_books):
        books_collector.add_book_in_favorites(HORROR_BOOK)
        assert books_collector.get_list_of_favorites_books() == [HORROR_BOOK]

    # Проверка добавления книги в избранное 2 раза
    def test_add_book_in_favorites_add_duplicate_book(self, books_collector, prepare_books):
        books_collector.add_book_in_favorites(HORROR_BOOK)
        books_collector.add_book_in_favorites(HORROR_BOOK)
        assert len(books_collector.get_list_of_favorites_books()) == 1

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_one_book_success(self, books_collector):
        books_collector.add_book_in_favorites(DETECTIVE_BOOK)
        books_collector.delete_book_from_favorites(DETECTIVE_BOOK)
        assert books_collector.get_list_of_favorites_books() == []

    # Проверка корректного вывода жанра книги по её имени
    def test_get_book_genre_get_genre_success(self, books_collector, prepare_books):
        assert books_collector.get_book_genre(COMEDY_BOOK) == 'Комедии'

    # Проверка корректности списка избранных книг
    def test_get_list_of_favorites_books_list_is_correct(self, books_collector, prepare_books):
        books_collector.add_book_in_favorites(FANTASY_BOOK)
        books_collector.add_book_in_favorites(DETECTIVE_BOOK)
        assert len(books_collector.get_list_of_favorites_books()) == 2