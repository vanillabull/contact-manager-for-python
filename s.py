import time

contacts = {}

def menu():
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Search for contacts")
    print("4. Exit")

def option_1():
    contact_num = input("Enter a contact number: ")
    name = input("Enter a name: ")
    contacts[contact_num] = name  # Store in dictionary
    print("Loading...")
    time.sleep(1)
    print("Contact saved!")

def option_2():
    if not contacts:
        print("No contacts to remove!")
        return
    print("Contacts:")
    for contact_num, name in contacts.items():
        print(f"{contact_num} - {name}")
    user_choice = input("Enter a contact number to remove: ")
    if user_choice in contacts:
        del contacts[user_choice]
        print("Contact removed!")
    else:
        print("Contact not found.")

def option_3():
    if not contacts:
        print("No contacts to search!")
        return
    user_choice = input("Search for a contact number: ")
    if user_choice in contacts:
        print(f"Contact found! Name: {contacts[user_choice]}")
    else:
        print("Contact not found.")

# --------- Menu options + Loop -----------

while True:
    menu()
    option = input("Select an option: ")

    if option == "1":
        option_1()
    elif option == "2":
        option_2()
    elif option == "3":
        option_3()
    elif option == "4":
        print("Exiting program...")
        break
    else:
        print("That is not a valid option")

    input("\nPress Enter to return to menu...")
