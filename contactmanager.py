contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number: ").lower()
    found = False
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            print(f"\nFound Contact:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
            found = True
    if not found:
        print(" No matching contact found.")

def update_contact():
    print("\n--- Update Contact ---")
    query = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == query:
            print("Leave blank to keep old value.")
            name = input(f"New Store Name ({contact['name']}): ") or contact['name']
            phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New Email ({contact['email']}): ") or contact['email']
            address = input(f"New Address ({contact['address']}): ") or contact['address']
            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    query = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == query:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main_menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
