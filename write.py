import datetime  # importing datetime for bill timestamps

#function to save product data to file
def save(d):
    """
    Saves product data to WeCare.txt.
    
    Args:
        dict: Dictionary containing product data.
    
    Returns:
        None
    """
    try:
        bill_text = ""  # initialize content string
        for item in d.values():  # loop through each product in dictionary
            line = ",".join(item)  # join product attribute with comma
            bill_text = bill_text + line + "\n"  # add line with newline
        file = open("WeCare.txt", "w")  # open file in write mode
        file.write(bill_text)  # write content to file
        
        file.close()  # closing the file
    except Exception as e:
        print("Error in file: " + e)  # handle errors

def generate_filename(bill_type):
    """
    Creates a unique filename using timestamp.
    
    Args:
        bill_type (str): Type of bill ('sale' or 'purchase').
    
    Returns:
        str: Unique filename.
    """
    now = datetime.datetime.now()  # get current date and time

    #formating the date and time as a string
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)

    #manually checking the two digitals for month, day, hour, minute, and second
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    if len(second) == 1:
        second = "0" + second

    return bill_type + "_" + year + month + day + "_" + hour + minute + second + ".txt"

def bill(bill_items, total, bill_type, name, phone, vat_amount, delivery_fee):
    """
    Creates and displays a bill, saving it to a uniquely named file.
    
    Args:
        bill_items (list): List of bill items.
        total (float): Total bill amount.
        bill_type (str): Type of bill ('sale' or 'purchase').
        name (str): Customer or manufacturer name.
        phone (str): Customer or manufacturer phone number.
        vat_amount (float): VAT amount for sales.
        delivery_fee (float): Delivery fee for sales.
    
    Returns:
        None
    """
    try:
        bill_text = ""  # initialize bill content
        
        bill_text = bill_text + "\t\t\t\tWeCare Wholesale Invoice \n"  # header
        bill_text = bill_text + "=" * 85 + "\n"  # separator
        bill_text = bill_text + "Customer Information:\n"  # customer details section
        bill_text = bill_text + "Name: " + name + "\n"  # name
        
        now = datetime.datetime.now()  # timestamp
        
        current_time = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        bill_text = bill_text + "Issued: " + current_time + "\n"  # timestamp
        bill_text = bill_text + "=" * 85 + "\n"  # separator
        bill_text = bill_text + "\nItems Purchased:\n"  # items section
        bill_text = bill_text + "Name\t\tBrand\t\tQty\tFree\tPrice\tTotal\n"  # header
        bill_text = bill_text + "=" * 85 + "\n"  # separator
        
        for row in bill_items:
            bill_text = bill_text + "\t".join(row) + "\n"  # adding each item in bill
        bill_text = bill_text + "=" * 85 + "\n"  # separator
        if bill_type == "sale":
            bill_text = bill_text + "VAT (13%): Rs. " + str(vat_amount) + "\n"  # VAT
            if delivery_fee > 0:
                bill_text = bill_text + "Delivery Charge: Rs. " + str(delivery_fee) + "\n"  # delivery
        bill_text = bill_text + "Grand Total: Rs. " + str(total) + "\n"  # total
        bill_text = bill_text + "\t\t\tThank You!\n"  # footer

        file = open(generate_filename(bill_type), "w")  # open file in write mode for bill
        file.write(bill_text)  # write content
        file.close()  # closing the file

        print("-" * 85)
        print("WeCare Wholesale Receipt")
        print("=" * 85)
        print("Customer Information:")
        print("Name: " + name)
        print("Issued: " + current_time)
        print("=" * 85)
        print("Items Purchased:")
        print("Name\t\tBrand\t\tQty\tFree\tPrice\tTotal")
        print("-" * 85)
        
        for row in bill_items:
            print("\t".join(row))  # display items
        print("-" * 85)
        if bill_type == "sale":
            print("VAT (13%): Rs. " + str(vat_amount))
            if delivery_fee > 0:
                print("Delivery Charge: Rs. " + str(delivery_fee))
        print("Grand Total: Rs. " + str(total))
        print("=" * 85)
    except Exception as e:
        print("Error while creating the bill: " + str(e))  # handle errors
