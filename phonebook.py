contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    
    
    contacts[name] = {'Phone': phone}
    print(f"Contact '{name}' added successfully!")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")

def edit_contact():
    name = input("Enter the contact name you want to edit: ")
    
    if name in contacts:
        phone = input("Enter new phone number: ")
        
        
        contacts[name]['Phone'] = phone
        
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the contact name you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def mainevent():
    while True:
        print("1-add_contact")
        print("2-display_contacts")
        print("3-edit_contact")
        print("4-delete_contact")
        print("5-exit \n")
        op = int(input("Enter your option:"))
        if op == 1:
            add_contact()
        elif op == 2:
            display_contacts()
        elif op == 3:
            edit_contact()
        elif op == 4:
            delete_contact()
        elif op == 5:
            break
        else:
            print("Invalid Option")

mainevent()



