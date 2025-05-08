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
'''
#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#custom imports
from Lib.Frequency import Frequency
#other imports
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

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
class Data_Frame(Frequency):
    def __init__(self):
        self.config = {
            'default_plot_type': 'histogram',
            'columns_to_plot': ['Flavor', 'Size', 'Topping', 'Price']
        }


        try:
            self.data = pd.read_csv('Input/data.csv')
            self.data.columns = self.data.columns.str.strip()  
        except FileNotFoundError:
            logger.error("Error: 'Input/data.csv' not found.")
            self.data = pd.DataFrame()
        except pd.errors.EmptyDataError:
            logger.error("Error: 'Input/data.csv' is empty or unreadable.")
            self.data = pd.DataFrame()
        except Exception as e:
            logger.error(f"Unexpected error loading CSV: {e}")
            self.data = pd.DataFrame()

        os.makedirs('output', exist_ok=True)
        print(self.data)

    def visualize_violin(self, column):
        """Visualize and save a plot for the given column based on its type."""
        if self.data.empty:
            logger.info("No data available to visualize.")
            return

        if column not in self.data.columns:
            logger.error(f"Error: Column '{column}' not found in dataset.")
            return

        
        plot_path = f'output/{column.lower()}_violin.png'
        temp = pd.DataFrame({column: self.data[column]})
        #plt.figure(figsize=(6,8))
        sb.violinplot(data = temp, y = column)
        plt.title(f'Distribution of {column}')
        plt.xlabel('Number Purchased')
        plt.ylabel(column)
        plt.savefig(plot_path)
        plt.close()
        
        logger.info(f"Plot for '{column}' saved to {plot_path}")

    def visualize_boxplot(self, column):
        if self.data.empty:
            logger.warning("No data available to visualize.")
            return

        if column not in self.data.columns:
            logger.error(f"Error: Column '{column}' not found in dataset.")
            return

        plot_path = f'output/{column.lower()}_boxplot.png'
        counts = self.data[column].value_counts()
        plt.boxplot(counts)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.xticks([])
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()
        logger.info(f"Plot for '{column}' saved to {plot_path}")

    def visualize_scatterplot(self, column1,column2, column3):
        if self.data.empty:
            logger.warning("No data available to visualize.")
            return

        if column1 not in self.data.columns:
            logger.error(f"Error: Column '{column1}' not found in dataset.")
            return
        
        if column2 not in self.data.columns:
            logger.error(f"Error: Column '{column2}' not found in dataset.")
            return

        plot_path = f'output/{column1.lower()}_{column2.lower()}_scatterplot.png'
        #counts = self.data[column].value_counts()
        #plt.plot(self.data[column1],self.data[column2],ls='',marker='o')
            
        plt.figure(figsize=(8,6))
        sb.scatterplot(data=self.data, x=column1, y=column2, hue = column3)
        plt.title(f'Distribution of {column1} per {column2} by {column3}')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.close()
        logger.info(f"Scatterplot saved to {plot_path}")

#Function definitions Start Here
def main():
    pass
#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    print(f"\"{Data_Frame}\" module begins.")
    main()

