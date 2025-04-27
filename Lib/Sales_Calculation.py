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
import logging
#other imports

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logging.basicConfig(
    filename=os.path.join('output','logs'),
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')
#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger = logging.getLogger(__name__)
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here

#Class definitions Start Here

#Function definitions Start Here
# Lib/Sales_Calculation.py

from Lib.Sales import Sales
import pandas as pd
from itertools import permutations, combinations
import matplotlib.pyplot as plt

class Sales_Calculation(Sales):
    def __init__(self, pickle_path='Input/data.pkl'):
        super().__init__(pickle_path)

    def joint_counts(self, col1, col2):
        if col1 not in self.data.columns or col2 not in self.data.columns:
            logger.error(f"One or both columns not found.")
            return None
        return pd.crosstab(self.data[col1], self.data[col2])

    def joint_probabilities(self, col1, col2):
        joint = self.joint_counts(col1, col2)
        if joint is not None:
            return joint / joint.values.sum()
        else:
            return None

    def conditional_probabilities(self, given_col, target_col):
        if given_col not in self.data.columns or target_col not in self.data.columns:
            logger.error(f"One or both columns not found.")
            return None
        return pd.crosstab(self.data[target_col], self.data[given_col], normalize='columns')

    def unique_values(self, col):
        if col not in self.data.columns:
            logger.error(f"Column '{col}' not found.")
            return []
        return self.data[col].unique()

    def generate_permutations(self, col, r=2):
        values = self.unique_values(col)
        return list(permutations(values, r))

    def generate_combinations(self, col, r=2):
        values = self.unique_values(col)
        return list(combinations(values, r))

    def plot_stacked_bar(self, given_col, target_col):
        if given_col not in self.data.columns or target_col not in self.data.columns:
            logger.error(f"One or both columns not found.")
            return

        try:
            cond_probs = pd.crosstab(self.data[target_col], self.data[given_col], normalize='columns')
            cond_probs.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

            plt.title(f'Stacked Bar Chart of {target_col} given {given_col}')
            plt.xlabel(target_col)
            plt.ylabel('Conditional Probability')
            plt.legend(title=given_col, bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.xticks(rotation=45)
            plt.tight_layout()

            output_file = f"{self.config['output_dir']}/StackedBar_{target_col}_given_{given_col}.png"
            plt.savefig(output_file)
            plt.close()
            logger.info(f"Saved: {output_file}")

        except Exception as e:
            logger.error(f"Error generating stacked bar chart: {e}")



def main():
    pass
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    print(f"\"{Sales_Calculation}\" module begins.")
    main()
