"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
    You are given a list of prices for items you want to buy and some money. How many items can you buy?

You should be able to start at any index in the list and work your way forwards. You buy the first item you can afford, then the second, and so on. If you run out of money or reach the end of the list, you stop. You should also be able to go through the list backwards in the same manner, stopping if you reach the start of the list.
Write a function that takes a list of prices and the amount of money you have and returns the number of items you can buy. Your function should be able to handle all three scenarios.

  Parameters
    prices (list) – list of prices

    money (int) – amount of money

    start_index (int) – starting index in list

    reverse (bool) – boolean to indicate if list should be run in reverse

    Return type
    int

    Returns
    number of items that can be bought with the given amount of money
"""

#Import the necessary libraries
import os  
import re

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")

def best_buy(prices, money, start_index, reverse):
    #test if reverse is true
    if reverse:
        #if reverse is true, we reverse the list
        prices = prices[::-1]
        #we also reverse the start index
        start_index = len(prices) - start_index - 1
    #we initialize the number of items to zero
    number_of_items = 0
    #we initialize the total price to zero
    total_price = 0
    #we initialize the index to the start index
    index = start_index
    #we initialize the while loop
    while index < len(prices) and total_price + prices[index] <= money:
        #we update the total price
        total_price += prices[index]
        #we update the number of items
        number_of_items += 1
        #we update the index
        index += 1
    return number_of_items

prices = [3, 2, 1, 3, 5]
print(best_buy(prices, 10, 0, False),best_buy(prices, 3, 1, False),best_buy(prices, 8, 4, True),best_buy(prices, 10, 4, True))
