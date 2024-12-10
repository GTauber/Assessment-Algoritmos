def find_contact(contacts, name):

    for contact in contacts:
        if contact['name'] == name:
            return contact['tel']
    return None

if __name__ == "__main__":
    contacts = [
        {'name': 'Renatão', 'tel': '1111-1111'},
        {'name': 'Ronaldão', 'tel': '2222-2222'},
        {'name': 'Renatinho', 'tel': '3333-3333'},
        {'name': 'Ronaldinho', 'tel': '4444-4444'},
    ]

    name = input("name of the contact: ")
    tel = find_contact(contacts, name)

    if tel:
        print(f"tel of {name} is {tel}.")
    else:
        print(f"contract {name} not found.")

