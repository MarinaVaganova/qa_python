import pytest


from data import fantasy_book, horror_book, detective_book, child_book, comedy_book


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # Проверка добавления 2-х книг с одинаковым названием
    def test_add_new_book_add_duplicate_book(self, books_collector):
        books_collector.add_new_book(child_book)
        books_collector.add_new_book(child_book)
        assert len(books_collector.get_books_genre()) == 1

    # Проверка добавления книги с названием более 40 символов
    def test_add_new_book_add_book_more_40_symbols(self, books_collector):
        books_collector.add_new_book('Сияние Сияние Сияние Сияние Сияниееееееее')
        assert len(books_collector.get_books_genre()) == 0

    # Проверка, что если жанр не входит в список genre, он не устанавливается
    def test_set_book_genre_invalid_genre(self, books_collector, prepare_books):
        books_collector.set_book_genre(fantasy_book, 'Биография')
        assert books_collector.books_genre[fantasy_book] != 'Биография'

    # Проверка вывода книги определенного жанра
    def test_get_books_with_specific_genre_book_get_list_genre(self, books_collector, prepare_books):
        genre = 'Фантастика'
        assert books_collector.get_books_with_specific_genre(genre) == [fantasy_book]

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
        assert books_collector.get_books_for_children() == [fantasy_book, child_book, comedy_book]

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites_add_one_book_success(self, books_collector, prepare_books):
        books_collector.add_book_in_favorites(horror_book)
        assert books_collector.get_list_of_favorites_books() == [horror_book]

    # Проверка добавления книги в избранное 2 раза
    def test_add_book_in_favorites_add_duplicate_book(self, books_collector, prepare_books):
        books_collector.add_book_in_favorites(horror_book)
        books_collector.add_book_in_favorites(horror_book)
        assert len(books_collector.get_list_of_favorites_books()) == 1

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_one_book_success(self, books_collector):
        books_collector.add_book_in_favorites(detective_book)
        books_collector.delete_book_from_favorites(detective_book)
        assert books_collector.get_list_of_favorites_books() == []
