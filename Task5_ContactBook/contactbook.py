

# Task 5 - Contact Book
contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added.")

def view_contacts():
    for name, info in contacts.items():
        print(f"{name}: {info}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(contacts[name])
    else:
        print("Not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted.")
    else:
        print("Not found")

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
    ch = input("Choice: ")
    if ch == "1": add_contact()
    elif ch == "2": view_contacts()
    elif ch == "3": search_contact()
    elif ch == "4": delete_contact()
    elif ch == "5": break
    else: print("Invalid")
