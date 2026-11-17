import json


def load_books():
  f = open("books.json", "r", encoding="utf-8")
  books = json.load(f)
  f.close()
  return books


def display_books():
  books = load_books()
  print("Список книг")
  for i, b in enumerate(books, 1):
    print(
        f"{i}. {b['title']} — {b['author']} ({b['year']})"
    )


def add_book():
  new_book = {
      "title": input("Название: "),
      "author": input("Автор: "),
      "year": int(input("Год издания: "))
  }
  books = load_books()
  books.append(new_book)
  
  f = open("books.json", "w", encoding="utf-8")
  json.dump(books, f, ensure_ascii=False, indent=4)
  f.close()
  print("Книга успешно добавлена!")

print("1 посмотреть книги 2 добавить книгу")
choice = input("Выбери действие: ")

if choice == "1":
  display_books()
elif choice == "2":
  add_book()
else:
  print("Неверный выбор.")
