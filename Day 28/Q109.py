books = []
def add_book():
    title = input("Enter book title: ")
    books.append(title)
    print("Book added.")
def view_books():
    for i, book in enumerate(books):
        print(f"{i+1}. {book}")
if __name__ == '__main__':
    while True:
        print("\n1. Add Book\n2. View Books\n3. Exit")
        c = input("Choice: ")
        if c == '1': add_book()
        elif c == '2': view_books()
        elif c == '3': break
