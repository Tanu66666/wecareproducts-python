from read import load  # importing load function
from operation import display, sales_, purchase_  # importing operation functions

def start():
    """
    Runs the main program with a menu for sales, purchases, and exit.
    
    Args:
        None
    
    Returns:
        None
    """
    print("")
    print("\t\t\t\t WeCare Wholesale System \t\t\t")
    print("=" * 85)
    print("")
    
    items = load()  # load inventory
    while True:  # main loop
        try:
            display(items, selling_price = False)  # displaying product list and cost prices
            print("")
            print("\t\t\t\t System Options \t\t")
            print("1. sell products")
            print("2. Restock Inventory")
            print("3. Exit ")
            print("=" * 85 + "\n")
            print("")
            
            choice = input("Choose from the option: ")  # takes user option input
            if len(choice) == 0:
                print("Option cannot be blank.")  # handle empty input
                continue
            if choice.isnumeric() == False:
                print("Option must be numeric.")  # handle non-numeric input
                continue
            choice = int(choice)
            if choice == 1:
                sales_(items)  # processing the sale
            elif choice == 2:
                purchase_(items)  # restocking
            elif choice == 3:
                print("Thank you for managing the system. Have a great day!")  # exit message
                break  # exiting the loop
            else:
                print("Option " + str(choice) + " is invalid. Please choose again.")  # invalid choice
        except Exception as e:
            print("System error: " + str(e))  # handle errors

#run the program
if __name__ == "__main__":
    start()  # start point of program
