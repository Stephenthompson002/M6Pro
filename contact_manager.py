"""
contact_manager.py

This file contains functions to manage contacts in the Contact Manager application.
It includes functionality to add, view, search, remove, and update contacts.
It also handles loading contacts from and saving contacts to a CSV file.

Functions:
- load_contacts(filename): Loads contacts from a CSV file into a list of dictionaries.
- save_contacts(contacts, filename): Saves contacts to a CSV file.
- add_contact(contacts): Prompts the user to add a new contact to the list.
- view_contacts(contacts): Displays all contacts in a tabular format.
- search_contact(contacts): Allows the user to search for a contact by name.
- remove_contact(contacts): Allows the user to remove a contact by name.
- update_contact(contacts): Allows the user to update the phone number of a contact by name.

"""

import csv
import re

def load_contacts(filename):
    """
    Loads contacts from the CSV file into a list of dictionaries.
    
    Pseudocode:
    1. Initialize an empty list to store contacts.
    2. Try to open the CSV file in read mode.
    3. If file exists, read the contents using the csv.DictReader to load the contacts.
    4. For each row in the CSV, append it to the contacts list.
    5. Return the contacts list.
    6. If the file is not found, handle the exception and return an empty list.

    Arguments:
    - filename: Name of the CSV file to load the contacts from.

    Returns:
    - contacts: List of dictionaries, each representing a contact.
    """
    contacts = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty contact list.")
    return contacts


def save_contacts(contacts, filename):
    """
    Saves the list of contacts to a CSV file.
    
    Pseudocode:
    1. Open the CSV file in write mode.
    2. Initialize a csv.DictWriter with the fieldnames for the CSV.
    3. Write the header row (column names).
    4. Write all contact rows to the CSV file.
    5. Close the file after writing.

    Arguments:
    - contacts: List of dictionaries representing contacts to be saved.
    - filename: Name of the CSV file to save the contacts to.
    """
    fieldnames = ['Full Name', 'phone', 'email']
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def is_valid_phone(phone):
    """
    Validates the phone number format (XXX)XXX-XXXX.
    
    Arguments:
    - phone: The phone number string to validate.

    Returns:
    - bool: True if the phone number is valid, False otherwise.
    """
    pattern = r'^\(\d{3}\)\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None


def add_contact(contacts):
    """
    Prompts the user to add a new contact to the contacts list.
    
    Pseudocode:
    1. Prompt the user to input the contact's full name, phone, and email.
    2. Validate the phone number using the is_valid_phone function.
    3. Validate the email to ensure it contains "@" and ".".
    4. Capitalize the full name properly using string methods.
    5. Create a dictionary with the contact's details and append it to the contacts list.
    6. Print a success message.

    Arguments:
    - contacts: List to which the new contact will be added.
    """
    full_name = input("Enter full name: ").strip().title()
    phone = input("Enter phone number (Format: (XXX)XXX-XXXX): ").strip()
    
    while not is_valid_phone(phone):
        print("Invalid phone format. Please follow the format (XXX)XXX-XXXX.")
        phone = input("Enter phone number (Format: (XXX)XXX-XXXX): ").strip()
    
    email = input("Enter email: ").strip()
    while "@" not in email or "." not in email:
        print("Invalid email. It must contain '@' and '.'.")
        email = input("Enter email: ").strip()
    
    contact = {"Full Name": full_name, "phone": phone, "email": email.lower()}
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts(contacts):
    """
    Displays all contacts in a tabular format.
    
    Pseudocode:
    1. Print the header row with column titles ("Full Name", "Phone", "Email").
    2. For each contact in the contacts list, print their details in tabular format.

    Arguments:
    - contacts: List of contacts to display.
    """
    if not contacts:
        print("No contacts available.")
        return
    
    print(f"{'Full Name':<20} {'Phone':<20} {'Email':<30}")
    print("-" * 70)
    for contact in contacts:
        print(f"{contact['Full Name']:<20} {contact['phone']:<20} {contact['email']:<30}")


def search_contact(contacts):
    """
    Allows the user to search for a contact by name (case-insensitive).
    
    Pseudocode:
    1. Prompt the user to enter a search term (name).
    2. Loop through each contact in the contacts list.
    3. If the search term matches any contact's full name (case-insensitive), display that contact's details.
    4. If no match is found, notify the user that the contact was not found.

    Arguments:
    - contacts: List of contacts to search through.
    """
    search_term = input("Enter the name of the contact to search for: ").strip().lower()
    found = False
    for contact in contacts:
        if search_term in contact['Full Name'].lower():
            print(f"Found: {contact['Full Name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found.")


def remove_contact(contacts):
    """
    Allows the user to remove a contact by name.
    
    Pseudocode:
    1. Prompt the user to enter the name of the contact to remove.
    2. Loop through each contact and check if the name matches.
    3. If a match is found, remove that contact from the contacts list.
    4. If no contact is found, notify the user.

    Arguments:
    - contacts: List of contacts from which a contact will be removed.
    """
    name_to_remove = input("Enter the name of the contact to remove: ").strip().title()
    for contact in contacts:
        if contact['Full Name'] == name_to_remove:
            contacts.remove(contact)
            print(f"Contact '{name_to_remove}' removed successfully.")
            return
    print(f"No contact found with the name '{name_to_remove}'.")


def update_contact(contacts):
    """
    Allows the user to update a contact's phone number by name.
    
    Pseudocode:
    1. Prompt the user to enter the name of the contact to update.
    2. Loop through each contact and check if the name matches.
    3. If a match is found, prompt the user to enter the new phone number.
    4. Validate the new phone number using the is_valid_phone function.
    5. Update the contact’s phone number in the contacts list.
    6. If no contact is found, notify the user.

    Arguments:
    - contacts: List of contacts to update.
    """
    name_to_update = input("Enter the name of the contact to update: ").strip().title()
    for contact in contacts:
        if contact['Full Name'] == name_to_update:
            new_phone = input("Enter the new phone number (Format: (XXX)XXX-XXXX): ").strip()
            while not is_valid_phone(new_phone):
                print("Invalid phone format. Please follow the format (XXX)XXX-XXXX.")
                new_phone = input("Enter the new phone number (Format: (XXX)XXX-XXXX): ").strip()
            contact['phone'] = new_phone
            print(f"Phone number for '{name_to_update}' updated successfully.")
            return
    print(f"No contact found with the name '{name_to_update}'.")
