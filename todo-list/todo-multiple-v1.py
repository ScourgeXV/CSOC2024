'''
This script is being used as a
single user TODO list.
We are using a static file to
Create Read Update Delete items
in this todo list
'''

__author__ = "Saatvic Sehgal"


def display_menu() :
    '''
    This function is used as the
    interface of this program. It
    displays a basic intro message
    and options available to the
    user to perform on their TODO
    list.
    '''
    print("_"*75,'\n')
    print("Welcome to My TODO List. Please select from below options.\n")
    print("1. Add an Item")
    print("2. View added Items")
    print("3. Update existing Item")
    print("4. Mark as Done")
    print("5. Exit")
    print('\n',"_"*75,'\n')


def add_item(items) :
    '''
    This functions is called whenever
    user wants to add any item to
    their TODO list. 
    '''
    item = input("Enter item description: ")
    items.append(item)
    print("Item added successfully!")
    save_items(items)


def view_items(items) :
    '''
    This functions is called whenever
    user wants to view their TODO list. 
    '''
    print("\nitems:")
    for i, item in enumerate(items, start=1) :
        print(f"{i}. {item}")
        

def update_item(items) :
    '''
    This functions is called whenever
    user wants to update any existing
    item in their TODO list. 
    '''
    if not items :
        print("No items to update.")
        return

    view_items(items)
    index = int(input("Enter item index to mark as done: ")) - 1
    updated_item = input("Enter the updated value: ")
    items[index] = updated_item
    save_items(items)


def mark_item_done(items) :
    '''
    This functions is called whenever
    user wants to mark any existing
    item as done in their TODO list. 
    '''
    if not items :
        print("No items to mark as done.")
        return

    view_items(items)
    index = int(input("Enter item index to mark as done: ")) - 1

    if 0 <= index < len(items) :
        removed_item = items.pop(index)
        print(f"item '{removed_item}' marked as done and removed.")
    else :
        print("Invalid item index.")
    save_items(items)


def save_items(items) :
    '''
    This functions is called whenever
    any changes made to file are needed
    to be saved in the file
    '''
    with open("items.txt", "w") as f:
        for item in items :
            f.write(item + '\n')


def load_items(name) :
    '''
    This function is called to read
    the file having TODO list of user
    and return the items in the form
    of a list.
    '''
    filename = name + ".txt"
    try :
        print("Login successful.")
        with open(filename, "r") as f :
            return f.readlines()
    except FileNotFoundError:
        print("No such user existed.")
        print("Created new user.")
        return []


def create_items(name) :
    filename = name + ".txt"
    try :
        f = open(filename,"r")
        print("OOPS!! User already exist. Please use different username")
        f.close()
        return 0
    except :
        f = open(filename,"w")
        f.close()
        print("Created new user.")
        return []

def main() :
    
    print("1. Existing User")
    print("2. New User")
    user = int(input("Are you Existing user/New user: "))
    name = input("Enter username:")
    if user == 1 :
        items = load_items(name)
    elif user == 2 :
        items = create_items(name)
        
    while True :
        display_menu()

        choice = input("Enter your choice: ")
        if choice == '1' :
            add_item(items)
        elif choice == '2' :
            view_items(items)
        elif choice == '3' :
            update_item(items)
        elif choice == '4' :
            mark_item_done(items)
        elif choice == '5' :
            print("Exiting.")
            save_items(items)
            break
        else :
            print("Invalid choice. Please select a valid option.")
        print()


if __name__ == "__main__" :
    main()
