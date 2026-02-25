# Contact Book 
contact = {}
while True:
    print("""Choose an option:
a. Add Contact
b. Search Contact
c. Show Contacts
d. Exit""")
    user = input("Enter the option you chose: ").strip().lower()

    if user == 'a':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        contact[name] = number
        print(f"Contact added: {name} : {number}")

    elif user == 'b':
        search = input("Enter the name you want contact of: ")
        if search in contact:
            print(f"{search} : {contact[search]}")
        else:
            print("Sorry! Not in Contact List")

    elif user == 'c':
        for k, v in contact.items():
            print(k,":",v)
        else:
            print("No contacts saved yet")
            

    elif user == 'd':
        print("Goodbye!")
        break

    else:
        print("Invalid option — please type a, b, c, or d.")
