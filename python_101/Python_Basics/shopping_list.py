#Tutorial from Criag Denis on https://teamtreehouse.com/
#with only minor changes.

def add_to_list(item):
    items.append(item)
    #TODO: maybe clear the screen here?
    print("\nItem added. Your list has {} items in it.\n".format(len(items)))

def show_help():
    print("""
Enter "done" to stop adding items.
Enter "help" to display options.
Enter "show" to display items currently in the list.
""")

def show_list():
    if items:
        print("\n----CURRENT LIST----\n")
        for item in items:
            print(item)
        print("\n")


items = []
print("\nWelcome to the list maker.")
show_help()
while True:
    print("What would you like to add to your list? ")
    item = input("#")

    if item.upper() == "DONE":
        break
    elif item.upper() == "HELP":
        show_help()
        continue
    elif item.upper() == "SHOW":
        show_list()
        continue
    else:
        add_to_list(item)

show_list() 