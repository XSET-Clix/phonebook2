contacts = {}
print("Welcome to Phonebook")
print("What do you want to do today?")
print("1.add")
print("2.remove")
print("3.update")
print("4.display")
print("5.exit")

def add():
    name = input("Enter your name:")
    number = int(input("Enter your number:"))
    if name in contacts:
        print("Name already exists.")
    else:
        contacts[name]=number
        print("Contacts saved")
        
def remove():
    name = input("Enter your name:")
    if name not in contacts:
        print("Name already deleted")
    else:
        del contacts[name]
        print("Contact Deleted")

def update():
    if name in contacts:
        name = input("Enter your name:")
        number = int(input("Enter your number:"))
        contacts[name]=number
        print("Contact updated")
    else:
        print("Contact is not found")
        
def display():
    print("contacts: ")
    for i in contacts:
        print( i, ":", contacts[i])
        print()

while True:
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        update()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Thank you using the Phonebook")
        break
    else:
        print("invaild option")