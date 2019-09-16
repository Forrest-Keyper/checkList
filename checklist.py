from termcolor import colored

checklist = list()

'''
checklist.append('Blue')
print(checkList)
checkList.append('Orange')
print(checkList)
'''
def create(item):
#Create code
    checklist.append(item)
def read(index):
#Read code
    print(checklist[index])

def update(index, item):
#Update code
    checklist[index] = item

def destroy(index):
#Destroy code
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(colored("The index of our {} is {}".format(list_item, index), 'magenta'))
        index+=1


def select(function_code):
    # Create item
    function_inputs = {}
    folded_functCode = function_code.casefold()
#create
    if (folded_functCode == "c"):
        #running = False
        input_item = user_input("Input item: ")
        create(input_item)
        print(("Added {} to checklist.").format(input_item))


    #update
    elif (folded_functCode == "u"):
        update_location = (int(user_input("Which item would you like to update? ")))
        update_item = user_input("What would you like to replace your selection with? ")
        update_index = int(update_location)
        update(update_index, update_item)
        list_all_items()

    #Read item
    elif (folded_functCode == "r"):
        item_index = (int(user_input("Which item to read? ")))
        read(item_index)
        destroy_item = (user_input("Would you like to remove this item? Y/N"))

        if(destroy_item.lower() == 'y'):
            destroy(item_index)
        else:
            return True
        #item_index must have value for program to function

    #view entire list
    elif (folded_functCode == "p"):
        list_all_items()

    elif (folded_functCode == "q"):
        return False


    else:
        print("Main Menu")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    '''
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)
    print("destroyed")
    print(read(0))
    list_all_items()
    #print(read(1))
    '''

    create("Starting Unicorn of Tutorial Spectacles")

    list_all_items()
    #select("R")
    #list_all_items()

test()

running = True
while running:
    selection = user_input("""
            Press
            C to add to list,
            R to read from list,
            U to update list
            P to display list
            """)
    select(selection)
