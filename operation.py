import datetime  # importing datetime for bill timestamps
from write import bill, save  # importing bill and save functions

def display(d, selling_price=False):
    """
    Shows available products in a table format.
    
    Args:
        dict: Dictionary containing product data.
        selling_price (bool): If True, show 200% selling price; else, cost price.
    
    Returns:
        None
    """
    if len(d) == 0:  # check for empty inventory
        print("No items in stock.")  # inform user
        return
    print("-" * 85)
    print("ID\tName\t\tBrand\t\tStock\tPrice\tOrigin")  # table header
    print("=" * 85)
    for key, value in d.items():  # loop through each item in dictionary
        price = str(float(value[3]) * 2) if selling_price else value[3]  # selling or cost price
        print(str(key) + "\t" + value[0] + "\t\t" + value[1] + "\t\t" + value[2] + "\t" + price + "\t" + value[4])
        print()#new line
    print("=" * 85)

def sales_(d):
    """
    Manages customer sales, updates inventory, and creates a bill.
    
    Args:
        dict: Dictionary containing product data.
    
    Returns:
        None
    """
    bill_items = []  # empty list to store bill items
    totalcost = 0  # total bill amount
    
    try:
        print("=" * 85)
        print("Customer Sale Process")
        print("Please provide customer details for billing.")
        print("=" * 85)
        
        name = input("Customer name: ")
        print("")

        phone = input("Customer phone number: ")
        print("")
        if len(phone) == 0:
            print("Invalid phone number.")
            phone = "0000000000"
        print("~" * 85)
        print("")
        while True:
            display(d, selling_price=True)  # show selling prices
            item_id = input("Enter product ID: ")  # get ID
            
            if len(item_id) == 0:
                print("ID cannot be blank.")  # handle empty input
                continue
            if item_id.isnumeric() == False:
                print("ID must be numeric.")  # handle non-numeric input
                continue
            item_id = int(item_id)  # convert to integer
            if item_id == 0:
                break  # exit loop
            if (item_id in d) == False:
                print("Product ID not found.")  # handle invalid ID
                continue

            quantity = input("Enter quantity to purchase: ")  # get quantity
            if len(quantity) == 0:
                print("Quantity cannot be blank.")  # handle empty input
                continue
            if quantity.isnumeric() == False:
                print("Quantity must be numeric.")  # handle non-numeric input
                continue
            
            quantity = int(quantity)  # convert to integer
            current_qty = int(d[item_id][2])  # get current stock
            if quantity <= 0:
                print("Quantity must be greater than zero.")  # handle non-positive
                continue
            free_units = quantity // 3  # calculating buy 3 get 1 free
            total_units = quantity + free_units  # total units with free units
            if total_units > current_qty:
                print("Not enough stock.")  # if the quantity is not enough, it will print 'not enough stock'
                continue

            print(name + ": You have received " + str(free_units) + " free items due to our buy 3 get 1 free offer.")
            d[item_id][2] = str(current_qty - total_units)  # update stock

            base_price = float(d[item_id][3])  # original price
            price_to_sell = base_price * 2  # 200% selling price
            total_price = quantity * price_to_sell  # price for total quantity

            # adding items to bill 
            bill_items.append([d[item_id][0], d[item_id][1], str(quantity), str(free_units), str(price_to_sell), str(total_price)])
            totalcost = totalcost + total_price  # update total cost

            sell_option = input("Do you want to add more items? (y/n): ")  # continue shopping
            if sell_option == "y":
                continue
            else:
                break

        if len(bill_items) > 0:  # process if items purchased
            confirm = input("Proceed with billing? (y/n): ")  # confirm bill
            if confirm == 'y':
                vat = totalcost * 0.13  # 13% VAT
                totalcost = totalcost + vat  # add VAT
                delivery_fee = 0
                delivery = input("Do you want to include delivery charge? (y/n): ")  # ask delivery
                if delivery == 'y':
                    delivery_input = input("Enter delivery charge amount: ")
                    if len(delivery_input) == 0:
                        print("Invalid charge. No delivery charge entered.")
                    else:
                        try:
                            delivery_fee = float(delivery_input)
                            if delivery_fee < 0:
                                print("Delivery charge cannot be negative.")
                            else:
                                totalcost = totalcost + delivery_fee
                        except ValueError:
                            print("Invalid charge. No delivery charge entered.")

                bill(bill_items, totalcost, "sale", name, phone, vat, delivery_fee)  # creating bill
                save(d)  # saving the updated stock
            else:
                print("Billing cancelled.")  # inform user
    except Exception as e:
        print("Sale process error: " + str(e))  # handle errors

def purchase_(d):
    """
    Manages purchases from manufacturers, updates inventory, and creates a bill.
    
    Args:
        d (dict): Dictionary containing product data.
    
    Returns:
        None
    """
    bill_items = []  # list for bill items
    totalcost = 0  # total bill amount
    
    try:
        print("*" * 85)
        print("Inventory Restock Process")
        print("Select products to restock.")
        print("-" * 85)
        
        display(d, selling_price=False)  # show cost prices
        while True:
            item_id = input("Enter product ID: ")  # getting product ID
            if len(item_id) == 0:
                print("ID cannot be blank.")  # handle empty input
                continue
            if item_id.isnumeric() == False:
                print("ID must be numeric.")  # handle non-numeric input
                continue
            item_id = int(item_id)  # convert to integer
            if item_id == 0:
                break  # exit loop
            if (item_id in d) == False:
                print("Product ID not found.")  # handle invalid ID
                continue

            quantity = input("Enter quantity to add: ")  # get quantity
            if len(quantity) == 0:
                print("Quantity cannot be blank.")  # handle empty input
                continue
            if quantity.isnumeric() == False:
                print("Quantity must be numeric.")  # handle non-numeric input
                continue
            quantity = int(quantity)  # convert to integer
            if quantity <= 0:
                print("Quantity must be greater than zero.")  # handle non-positive
                continue

            new_price = input("Enter new cost price: ")  # taking new cost price of the item
            current_qty = int(d[item_id][2])  # get current stock
            d[item_id][2] = str(current_qty + quantity)  # updating stock
            
            if len(new_price) > 0:
                try:
                    float(new_price)  # validate price
                    d[item_id][3] = new_price  # update price
                except ValueError:
                    print("Invalid price. Current price retained.")

            base_price = float(d[item_id][3])  # purchase price
            total_price = quantity * base_price  # total for quantity

            # adding items to bill
            bill_items.append([d[item_id][0], d[item_id][1], str(quantity), "0", str(base_price), str(total_price)])
            totalcost = totalcost + total_price  # update total

        if len(bill_items) > 0:  # process if items purchased
            confirm = input("Do you want to proceed with billing? (y/n): ")  # confirm bill
            if confirm == 'y':
                bill(bill_items, totalcost, "purchase", "Manufacturer", "0000000000", 0.0, 0.0)  # create bill
                save(d)  # save updated stock
            else:
                print("Billing cancelled.")  # inform user
    except Exception as e:
        print("Restock process error: " + str(e))  # handle errors
