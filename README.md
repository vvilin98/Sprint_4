# Тема "Юнит-тестирование" курс ЯндексПрактикум | qa_python_4
Для тестирования выбран класс `BooksCollector` который работает с книгами

Класс `BooksCollector` содержит:

- Словарь `books_genre`  `Название книги: Жанр книги`.
- Список `favorites` избранные книги.
- Список `genre` доступные жанры.
- Список `genre_age_rating`жанры с возрастным рейтингом.
- Набор методов для работы со словарем `books_genre` и списком `favorites`:
    - `add_new_book` — добавляет новую книгу в словарь без указания жанра.
    - `set_book_genre` — устанавливает жанр книги
    - `get_book_genre`— выводит жанр книги по её имени.
    - `get_books_with_specific_genre`— выводит список книг с определённым жанром.
    - `get_books_genre`— выводит текущий словарь `books_genre`.
    - `get_books_for_children` — возвращает книги, которые подходят детям.
    - `add_book_in_favorites` — добавляет книгу в избранное.
    - `delete_book_from_favorites` — удаляет книгу из избранного.
    - `get_list_of_favorites_books` — получает список избранных книг.

Для каждого из методов были написаны тесты. 

  - Метод `add_new_book` :
    - `test_add_new_book_add_two_books` - Проверка, что в словарь с книгами, были добавлены две книги.
    - `test_add_new_book_add_negative_book` - Проверка, что в словарь не добавляются книги, название которых превышает 40 символов. А так же книги без названия.
  - Метод `set_book_genre` 
    - `test_set_book_genre_added_genre_book_positive_result` - Проверка, что книге в словаре устанавливается жанр.
    - `test_set_book_genre_add_genre_is_not_list` - Првоерка, что книге в словаре не устанавливается жанр которого нет в листе доступных жанров.
  - Метод `get_book_genre`
    - `test_get_book_genre_for_name_positive_result` - Проверка, что метод `get_book_ganre` возвращает жанр согласно введенному наименованию книги.
  - Метод `get_books_with_specific_genre`
    - `test_get_books_with_specific_genre_get_two_books_detectiv` -  Проверка, что возвращается выборка книг только с жанром "Детектив"
  - Метод `get_books_genre`
    - `test_add_new_book_add_two_books`
  - Метод `get_books_for_children`
    - `test_get_books_for_children_two_books` - Проверка, что возвращается выборка книг только подходящее для детей
  - Метод `add_book_in_favorites` 
    - `test_add_book_in_favorites_add_one_book` - Проверка успешного добавление книги в `favorites` если данная книга присутствует в `books_genre`
    - `test_add_book_in_favorites_add_two_double_book` - Проверка, что в `favorites` не добавится книга которая уже там присутствует 
  - Метод `delete_book_from_favorites` 
    - `test_delete_book_from_favorites` - Тест проверяет удаление книги из `favorites`
  - Метод `get_list_of_favorites_books`
    - `test_add_book_in_favorites_add_one_book`

### Запустить все тесты
```bash
pytest -v test_tests.py
```

### Оценка покрытия
```bash
pytest --cov=main
```
