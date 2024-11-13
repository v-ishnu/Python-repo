# Scenario: Implement a contact management system using a dictionary where:
# The key is the contact’s name, and the value is the phone number.
# Allow the user to add, delete, and update contacts.
# Allow searching for a contact by name to get the phone number.
# Display all contacts in alphabetical order.
# Bonus: Allow storing multiple phone numbers for a contact by making the value a list.

contacts = {}

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone_number = int(input("Enter phone number: "))
        if name in contacts:
            contacts[name].append(phone_number)
        else:
            contacts[name] = [phone_number]
        print(f"Contact '{name}' added successfully.")

    elif choice == "2":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "3":
        name = input("Enter contact name to update: ")
        if name in contacts:
            new_phone_number = int(input("Enter phone number: "))
            contacts[name] = [new_phone_number]
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "4":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"Phone number(s) for '{name}': {contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == "5":
        sorted_names = sorted(contacts.keys())
        print("\nContacts:")
        for name in sorted_names:
            print(f"{name}: {contacts[name]}")

    elif choice == "6":
        print("Exiting contact management system.")
        break
    else:
        print("Invalid choice. Please try again.")