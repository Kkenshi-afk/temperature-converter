Data_file="phone_book.txt"

def load_book():
    book = {}
    try:
        with open(Data_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, number = line.split(":", 1) 
                book[name] = number
    except FileNotFoundError:
        book = {}
    return book
def save_book(book):
    with open(Data_file, "w", encoding="utf-8") as f:
        for name, number in book.items():
            f.write(f"{name}:{number}\n")
def add_contact(book, name, number):
    if name in book:
        print("This name already exists!")
        return False
    book[name] = number
    return True
def remove_contact(book, name):
    return book.pop(name, None) is not None

def find_contact(book, name):
    return book.get(name)

def list_contacts(book):
    for name, num in sorted(book.items()):
        print(f"{name}: {num}")

if __name__ == "__main__":
    phonebook = load_book()

    print("Adding record...")
    add_contact(phonebook, "Alice", "0533 000 00 00")
    add_contact(phonebook, "Bob", "0532 111 11 11")

    print("\nPeople in contacts:")
    list_contacts(phonebook)

    print("\nFind Bob:", find_contact(phonebook, "Bob"))

    print("\nAlice is being deleted...")
    remove_contact(phonebook, "Alice")

    print("\nFinal guide:")
    list_contacts(phonebook)

    save_book(phonebook)