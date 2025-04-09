#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
Data_Frame = 'DataFrame'
'''
Version: v0.1
Description:
    this child class of the parent class "frequency", will read from the input .....csv file that stores all of our order information
    - the orders are broken into columns with size, flavor, toppings, and price
    - the rows are the order numbers themselves

  to vizualize the data using violin plots, whisker-box plots, and scatter plots, the data from each column will be broken up and compare between the rows
    - since there is a variety of ways the compare orders, we can look at individual elements, or combination of elements to compare using different plots

  to query the data for search and display, we can set multiple conditions to compare each rows
    - such as if a snowball is a size "L" and flavor "tiger blood"
    - this is done by using & or || expressions to ensure that we are setting the data to be compared by more than one condition
      - this can set each row value to true or false depending on this boolean expression
Authors:
    Tyler Guidry, Brandon Stromeyer
Date Created : 4-7-2025
Date Last Updated: 4-7-2025
Doc:
    <***>
Notes:
    Applying the templete
###############################################################################################################################
Version: v0.1
Description:
    this class will measure the frequency of each flavor bought, regardless of size or topping
        - we will so this using a histogram to find the distribution/frewuency differences between the different flavors

    to query this data for searching, we will read our data from the csv file with all of the order information on it
        - this will allow us to scan for each instance of a particular flavor and keep track of how many times they appear
Authors:
    Tyler Guidry, Brandon Stromeyer
Date Created : 4-7-2025
Date Last Updated: 4-7-2025
Doc:
    <***>
'''
#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")
#
#custom imports

#other imports

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here

#Class definitions Start Here
class Frequncy:
    data = 0

class Data_Frame(Frequncy):
    data = 0

#Function definitions Start Here
def main():
    pass
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name_gl}\" module begins.")
    main()

