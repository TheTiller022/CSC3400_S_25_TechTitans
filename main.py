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
import logging
#
#custom imports
#import Input.Input_Module
#import Lib.Data_Frame
#import Lib.Sales_Calculation
#other imports
from Lib.Frequency import Frequency
from Lib.Data_Frame import Data_Frame
#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logging.basicConfig(
    filename=os.path.join('output','logs'),
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here
logger = logging.getLogger(__name__)
#Class definitions Start Here
#Function definitions Start Here
def main():
    f = Frequency()

    columns_to_plot = ['Flavor', 'Size', 'Topping', 'Price']
    for col in columns_to_plot:
        print(f"Generating plot for {col}...")
        f.visualize_column(col)

    print("\nStrawberry Orders:")
    result = f.query_data('Flavor', 'Strawberry')
    print(result)

    d = Data_Frame()
    d.visualize_violin('Flavor')
    d.visualize_boxplot('Size')
    d.visualize_scatterplot('Flavor','Price')
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    #print(f"\"{module_name_gl}\" module begins.")
    main()
