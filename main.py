#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
Sales = 'Lib/Sales'
'''
Version: v0.1
Description:
    main calls information from input and libaries and thus need to me imported
Authors:
    Tyler Poirrier, Brandon Stromeyer
Date Created : 4-7-2025
Date Last Updated: 4-7-2025
Doc:
    <***>
Notes:
    Applying the templete
'''
#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    #os.chdir("./../..")
#
#custom imports
import Input.Input_Module
import Lib.Data_Frame
import Lib.Sales_Calculation
#other imports

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here

#Class definitions Start Here
# main.py

from Lib.Frequency import Frequency

def main():
    f = Frequency()

    columns_to_plot = ['Flavor', 'Size', 'Topping', 'Price']
    for col in columns_to_plot:
        print(f"Generating plot for {col}...")
        f.visualize_column(col)

    print("\nStrawberry Orders:")
    result = f.query_data('Flavor', 'Strawberry')
    print(result)

if __name__ == '__main__':
    main()

#Function definitions Start Here
def main():
    pass
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name_gl}\" module begins.")
    main()
