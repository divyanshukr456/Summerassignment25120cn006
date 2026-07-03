def mini_lib():
    books = []
    while True:
        print("\n1. Issue Book\n2. Return Book\n3. View Books\n4. Exit")
        c = input("Choice: ")
        if c == '1': books.append(input("Book name: "))
        elif c == '2':
            b = input("Book name: ")
            if b in books: books.remove(b)
        elif c == '3': print(books)
        elif c == '4': break
if __name__ == '__main__':
    mini_lib()
