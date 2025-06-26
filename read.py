import datetime  # importing datetime to work with date and time

#function to load product datafrom the text file into a dictionary
def load():
    """
    Loads product data into a dictionary from WeCare.txt.
    
    Args:
        None
    
    Returns:
        dict: Dictionary with product IDs as keys and details as values.
    """
    d = {}  #empty dictionary to hold product data
    try:
        file = open("WeCare.txt", "r")# open file in read mode
        data = file.readlines()  #read all lines into a list
        
        file.close()  # closing the file
        
        ID = 1  # initialize the product ID
        for line in data:
            line = line.replace("\n", "").split(",")  # Remove new line and spliting by comma
            d[ID] = line  # assign line data to dictionary with ID
            ID = ID + 1  # increment ID for next item
    except FileNotFoundError:
        print("File not found. Ensure 'WeCare.txt' exists.")  # handle missing file
    except Exception as e:
        print("Error in file: " , e)  # handle other errors
    return d  # returning the dictionary contaning product 
