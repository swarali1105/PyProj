class PhoneBook:
    def __init__(self):
        self.stack = []

    def add_number(self, name, number):
        self.stack.append((name, number))

    def search_number(self, name):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == name:
                return self.stack[i][1]
        return None

phone_book = PhoneBook()

while True:
    choice = input('Enter 1 to add a phone number, 2 to search for a phone number, or q to quit: ')

    if choice == '1':
        name = input('Enter name: ')
        number = input('Enter phone number: ')
        phone_book.add_number(name, number)
        print('Phone number added.')
    elif choice == '2':
        name = input('Enter name: ')
        number = phone_book.search_number(name)
        if number is None:
            print('Phone number not found.')
        else:
            print('Phone number:', number)
    elif choice == 'q':
        break
    else:
        print('Invalid choice.')
