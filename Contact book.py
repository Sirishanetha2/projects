# Contact book dictionary to store contacts
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact_book[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"\n{name} has been added to your contact book.")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("\nYour contact book is empty.")
    else:
        print("\nContact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    query = input("Enter name or phone number to search: ")
    
    for name, details in contact_book.items():
        if name == query or details['phone'] == query:
            print(f"\nContact found: \nName: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("\nContact not found.")

# Function to update a contact's details
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    
    if name in contact_book:
        phone = input("Enter new phone number (leave blank to keep unchanged): ")
        email = input("Enter new email (leave blank to keep unchanged): ")
        address = input("Enter new address (leave blank to keep unchanged): ")
        
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        if address:
            contact_book[name]['address'] = address
            
        print(f"\n{name}'s contact details have been updated.")
    else:
        print("\nContact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contact_book:
        del contact_book[name]
        print(f"\n{name} has been deleted from your contact book.")
    else:
        print("\nContact not found.")

# Main program loop
def contact_book_app():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting Contact Book.")
            break
        else:
            print("\nInvalid choice, please try again.")

# Run the contact book application
contact_book_app()
