"""
main.py

This file contains the main program loop, which displays a menu of options for the user and handles interactions.
It calls functions from contact_manager.py to manage contact information.

Functions:
- main(): Starts the program and displays menu options in a loop until the user exits.

"""

import contact_manager

def main():
    """
    Starts the Contact Manager program, loads contacts, and displays a menu with options for the user
    to add, view, search, remove, and update contacts. The program continues in a loop until the user
    chooses to exit, at which point contacts are saved back to the CSV file.

    Pseudocode:
    1. Load contacts from the CSV file using the contact_manager's load_contacts function.
    2. Display a success message indicating contacts were loaded.
    3. Enter an infinite loop to display menu options and handle user input.
       a. Display menu options for adding, viewing, searching, removing, updating, or exiting.
       b. Prompt the user to input their choice.
       c. Use try-except block to handle user input:
          i. If choice is 1, call add_contact function to add a new contact.
          ii. If choice is 2, call view_contacts to display all contacts.
          iii. If choice is 3, call search_contact to search for a contact by name.
          iv. If choice is 4, call remove_contact to delete a contact by name.
          v. If choice is 5, call update_contact to modify a contact's phone number.
          vi. If choice is 6, save all contacts back to CSV, display a success message, and exit.
          vii. If the choice is not between 1 and 6, notify the user of invalid choice.
          viii. If user input is not an integer, catch the exception and notify the user.
    """

    # Step 1: Load contacts from the CSV file
    contacts = contact_manager.load_contacts("contacts.csv")
    print("Contacts loaded successfully.")

    # Step 3: Enter an infinite loop for the menu system
    while True:
        # Step 3a: Display the menu
        print("\nContact Manager Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Update Contact")
        print("6. Exit")

        try:
            # Step 3b: Get the user's menu choice
            choice = int(input("Enter your choice (1-6): "))

            # Step 3c: Handle each menu choice
            if choice == 1:
                # Add a new contact
                contact_manager.add_contact(contacts)
            elif choice == 2:
                # View all contacts
                contact_manager.view_contacts(contacts)
            elif choice == 3:
                # Search for a contact by name
                contact_manager.search_contact(contacts)
            elif choice == 4:
                # Remove a contact by name
                contact_manager.remove_contact(contacts)
            elif choice == 5:
                # Update a contact's phone number
                contact_manager.update_contact(contacts)
            elif choice == 6:
                # Save contacts and exit the program
                contact_manager.save_contacts(contacts, "contacts.csv")
                print("Contacts saved successfully. Exiting...")
                break
            else:
                # Step 3c vii: Handle invalid choice numbers
                print("Invalid choice. Please choose a number between 1 and 6.")

        except ValueError:
            # Step 3c viii: Handle non-integer input errors
            print("Invalid input. Please enter a number.")

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
