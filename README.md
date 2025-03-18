# Sprint_4

### Описание проекта
Приложение BooksCollector позволяет установить жанр книг и добавить их в избранное.

### Структура проекта
1. Класс BooksCollector: main.py
2. Тесты: tests.py
3. Фикстуры: conftest.py
   
### Методы и их тестовое покрытие
1. ```add_new_book:``` test_add_new_book_add_duplicate_book (Проверка добавления 2-х книг с одинаковым названием), test_add_new_book_add_book_more_40_symbols (Проверка добавления книги с названием более 40 символов)
2. ```set_book_genre:``` test_set_book_genre_get_genre_success (Проверка установки корректного жанра для книги)
3. ```get_book_genre:``` test_set_book_genre_get_genre_success (Проверка установки корректного жанра для книги)
4. ```get_books_with_specific_genre:``` test_get_books_with_specific_genre_book_get_list_genre (Проверка вывода книги определенного жанра)
5. ```get_books_genre:``` test_add_new_book_add_duplicate_book (Проверка добавления 2-х книг с одинаковым названием), test_add_new_book_add_book_more_40_symbols (Проверка добавления книги с названием более 40 символов), test_get_books_genre_empty (Проверка вывода пустого словаря, если в коллекции нет книг), test_get_books_genre_different_books_and_genres (Проверка корректного вывода словаря для разных книг и жанров)
6. ```get_books_for_children:``` test_get_books_for_children_three_books_get_list_books (Проверка списка книг, подходящих детям)
7. ```add_book_in_favorites:``` test_add_book_in_favorites_add_one_book_success (Проверка добавления книги в избранное), test_add_book_in_favorites_add_duplicate_book (Проверка добавления книги в избранное 2 раза), test_delete_book_from_favorites_delete_one_book_success (Проверка удаления книги из избранного)
8. ```delete_book_from_favorites:``` test_delete_book_from_favorites_delete_one_book_success (Проверка удаления книги из избранного)
9. ```get_list_of_favorites_books:``` test_add_book_in_favorites_add_one_book_success (Проверка добавления книги в избранное), test_add_book_in_favorites_add_duplicate_book (Проверка добавления книги в избранное 2 раза), test_delete_book_from_favorites_delete_one_book_success (Проверка удаления книги из избранного)
