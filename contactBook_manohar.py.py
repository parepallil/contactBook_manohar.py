class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def get_details(self):
        return {'Name': self.name, 'Phone': self.phone, 'Email': self.email}


if __name__ == "__main__":
    contact_list = []

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            name = input("Enter the name:")
            phone = input("Enter the phone number:")
            email = input("Enter the email address:")
            new_contact = Contact(name, phone, email)
            contact_list.append(new_contact)
            print(f"Contact {name} added successfully!")

        elif choice == 2:
            if not contact_list:
                print("No contacts found.")
            else:
                print("Contacts:")
                for contact in contact_list:
                    details = contact.get_details()
                    for key, value in details.items():
                        print(f'{key}: {value}',end=" ")
                    print()

        elif choice == 3:
            if not contact_list:
                print("No contacts found.")
            else:
                search_name = input("Enter the name to search:")
                found = False
                for contact in contact_list:
                    if contact.name == search_name:
                        details = contact.get_details()
                        for key, value in details.items():
                            print(f'{key}: {value}',end=" ")
                        print()
                        found = True
                        break
                if not found:
                    print(f"No contact found with the name {search_name}.")

        elif choice == 4:
            print("Goodbye!")
            exit()
