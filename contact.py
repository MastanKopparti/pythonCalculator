# Contact Book Application
contacts = {}
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    print(f"\nContact '{name}' added successfully!")
def view_contacts():
    if not contacts:
        print("\nNo contacts to display.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"- {name}: {details['Phone']}")
def search_contact():
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            print(
                f"\nFound Contact:\nName: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            found = True
            break
    if not found:
        print("\nContact not found.")
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Enter new details (leave blank to keep existing):")
        phone = input(f"New phone number [{contacts[name]['Phone']}]: ").strip()
        email = input(f"New email address [{contacts[name]['Email']}]: ").strip()
        address = input(f"New address [{contacts[name]['Address']}]: ").strip()
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print(f"\nContact '{name}' updated successfully!")
    else:
        print("\nContact not found.")
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"\nContact '{name}' deleted successfully!")
    else:
        print("\nContact not found.")
def main():
    print("Welcome to the Contact Book App! 📒")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ").strip()
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
            print("\nThank you for using the Contact Book! Goodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
