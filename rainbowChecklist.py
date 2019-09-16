def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    #Read item
    elif function_code == "R":
        item_index = user_input("Index number?")

        #item_index must have value for program to function
        read(item_index)
    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown Option")


    
