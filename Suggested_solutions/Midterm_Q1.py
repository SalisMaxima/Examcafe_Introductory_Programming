"""Made by: Mathias Herløv Lund 03/12/2023 
    Description:
       Compound interest is a term from banking. The formula for compound interest 𝐼 after one year is
        𝐼 = 𝑃
        (︁
        1 +
        𝑟
        𝑛
        )︁𝑛
        − 𝑃.
        Here, 𝑃 is the principal sum, 𝑟 is the interest rate (in decimals e.g., 4% is given as 𝑟 = 0.04), and 𝑛 is the compounding
        frequency.
        You should write a function that takes as input three numbers: principal for the principal sum, rate for the interest
        rate, and frequency for the compounding frequency. The function should return the compound interest after one

    Parameters:
        • principal (int) – A positive integer, the principal sum.
        • rate (float) – A positive float, the interest rate.
        • frequency (int) – A positive integer, the compounding frequency.
    Return type:
    float

    Returns:
    The compound interest.
"""
#Import the necessary libraries
import os  

#Find directory of python file
path=os.path.dirname(os.path.abspath(__file__))
#Change directory
os.chdir(path)

#os.chdir("C:/Users/mathi/Documents/GitHub/Examcafe_Introductory_Programming/Suggested_solutions")

def compound_interest(principal, rate, frequency):
    return principal * ((1 + rate/frequency)**frequency - 1)

#Test the function
print(compound_interest(1500, 0.04, 8)
)

#Another test
print(compound_interest(1000, 0.1, 2)
)

#Another test
print(compound_interest(1000, 0.1, 1)
)

#Compare output of function with expected output
print("The absolute error is: {}".format(abs(compound_interest(1500, 0.04, 8) - 61.06056588815591)))
print("The relative error is: {}%".format(abs(compound_interest(1500, 0.04, 8) - 61.06056588815591)/(61.06056588815591)*100))
