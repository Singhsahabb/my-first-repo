import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email} - {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact added: {new_contact}")

    def view_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        search_results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower()]
        if search_results:
            print("Search Results:")
            for contact in search_results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        contact_to_update = None
        for contact in self.contacts:
            if contact.name == name:
                contact_to_update = contact
                break
        if contact_to_update:
            if new_phone:
                contact_to_update.phone = new_phone
            if new_email:
                contact_to_update.email = new_email
            if new_address:
                contact_to_update.address = new_address
            print(f"Contact updated: {contact_to_update}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact_to_delete = None
        for contact in self.contacts:
            if contact.name == name:
                contact_to_delete = contact
                break
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print(f"Contact deleted: {contact_to_delete}")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter search term: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone = input("Enter new phone number (or enter to keep the same): ")
            new_email = input("Enter new email (or enter to keep the same): ")
            new_address = input("Enter new address (or enter to keep the same): ")
            contact_book.update_contact(name, new_phone, new_email, new_address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()