#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
Sales_Calculation = 'Sales_Calculation'
'''
Version: v0.1
Description:
    this class will start by reading the data from the Dataframe we made in Dataframe.py (child class 1)
  it will also be able to vizualize specific data depending on what the user inputs 

    - joint count will measure how many times 2 conditions occur together (aka small and tigerblood)
    - joint probability will divide the count of each instance and divide it by the total number of orders to figure out the probability that someone
    would order it
    - conditional probability will normalize the data by dividing it by the total count, then compare it to another column to see when it is most
    likely to occur
    - we will then use the functions defined in the parent Sales class to calculate mean, median, mode, and std
      - this can be done based on any condition defined by the user 

    - obtain position vector
      - this will grab each row of the table and identify it as a vector
        - this will include all columns / data for each order
    - obtain unit vectors
      - this will normalize the vector in order to compare it to other vectors
        - this allows us to do dot product in the next steps
    - obtain projection vectors
      - this can allow us to compare the 'alignment' of a vector compared to typical orders
        - this more or less means we can pull individual orders and see how it strays away from an average vector
    - calculate dot product
      - dot product will allow us to compare specific variations to the price of the order, the similarity between 2 orders, or certain trends in the data
Authors:
    Tyler Guidry, Brandon Stromeyer
Date Created : 4-7-2025
Date Last Updated: 4-7-2025
Doc:
    <***>
Notes:
    Applying the templete

###########################################################################################################################

Version: v0.1
Description:
    the second parent class, Sales, will define the utility functions used by the child class
    - mean will calculate the average apperances of a desired element
    - median will calculate the middle value of numerical data such as price
      - after the data is sorted
    - mode will calculate which of the desired variation information appears the most often
    - the standard deviation (std) will find the value of how far the data is from the mean (average)
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
class Sales:
    sales = 0
    
class Sales_Calculations(Sales):
    sales = 0
#Function definitions Start Here
def main():
    pass
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name_gl}\" module begins.")
    main()
