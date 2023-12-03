"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
        When customers visit a webshop page for a certain product, they see information about the stock status. This information
    is based on two numbers: number_of_items, the number of items currently in stock; and days_to_delivery, the
    number of days until delivery of new items from the factory, where 0 indicates that new items are not expected.
    Displayed text Stock situation
    In stock 6 or more items in stock
    Only <n> left in stock Between 1 and 5 items in stock. Here <n> is the number of items in
    stock.
    Available in <d> days No items in stock, but new items are expected. Here <d> is the number
    of days to delivery.
    Out of stock No items in stock, and no new items are expected.
    Unknown Either number of items is negative, or there are no items in stock, and
    the number of days to delivery is negative

    Input:  This information
            is based on two numbers: number_of_items, the number of items currently in stock; and days_to_delivery, the
            number of days until delivery of new items from the factory, where 0 indicates that new items are not expected.
    
    Output: The function should
            return the string with the text to be displayed.
"""
#Import the necessary libraries
import os  

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")

def stock_status(number_of_items, days_to_delivery):
    if number_of_items >= 6:
        return 'In stock'
    elif number_of_items >= 1:
        return 'Only ' + str(number_of_items) + ' left in stock'
    elif days_to_delivery >= 1:
        return 'Available in ' + str(days_to_delivery) + ' days'
    elif number_of_items == 0 and days_to_delivery == 0:
        return 'Out of stock'
    else:
        return 'Unknown'
    
#Test the function
print(stock_status(4, 7))

#Another test
print(stock_status(0, 0))

#Another test
print(stock_status(0, 1))
