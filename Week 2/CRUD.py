items = ['T-Shirt', 'Sweater']

while True:
    inp = input("Welcome to our shop, what do you want (C, R, U, D)? ")

    try:
        if inp == "C":
            new_item = input("Enter new item: ")
            items.append(new_item)
            print ("Our items:",", ".join(items))
            
        elif inp == "R":
            print ("Our items:",", ".join(items))

        elif inp == "U":
            update_position = int(input("Update position? "))
            new_item_for_replace = input("New item? ")
            items[update_position] = new_item_for_replace
            print ("Our items:",", ".join(items))

        elif inp == "D":
            delete_position = int(input("Delete position? "))
            items.pop(delete_position)
            print ("Our items:",", ".join(items))

        else:
            print ("You must choose in the list of characters (C, R, U, D)!")

    except Exception as ex:
        print ("The error","\""+str(ex)+"\"","has been found, please try again!")
