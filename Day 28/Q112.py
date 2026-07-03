contacts = {}
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    print("Contact saved.")
def view_contacts():
    for n, p in contacts.items(): print(f"{n} -> {p}")
if __name__ == '__main__':
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        c = input("Choice: ")
        if c == '1': add_contact()
        elif c == '2': view_contacts()
        elif c == '3': break
