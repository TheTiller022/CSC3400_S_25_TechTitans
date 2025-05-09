#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
Frequency = 'Frequency'
'''
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
Notes:
    Applying the templete
###############################################################################################################################
'''
#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os 
    #os.chdir("./../..")

#
#custom imports
import os
import pandas as pd
import matplotlib.pyplot as plt
import logging

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logging.basicConfig(
    filename=os.path.join('output','logs'),
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a')
#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
logger = logging.getLogger(__name__)
#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Class definitions Start Here
# Parent class 1

class Frequency:
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

    def visualize_column(self, column):
        if self.data.empty:
            logger.warning("No data available to visualize.")
            return

        if column not in self.data.columns:
            logger.warning(f"Error: Column '{column}' not found in dataset.")
            return

        plot_path = f'output/{column.lower()}_distribution.png'

        try:
            if column == 'Price':
                self.data[column].plot(kind='line', marker='o', color='green')
                plt.title(f'Line Plot of {column}')
                plt.xlabel('Index')
                plt.ylabel(column)
            else:
                counts = self.data[column].value_counts()
                counts.plot(kind='bar', color='skyblue')
                plt.title(f'Distribution of {column}')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.xticks(rotation=45)

            plt.tight_layout()
            plt.savefig(plot_path)
            plt.close()
            logger.info(f"Plot for '{column}' saved to {plot_path}")

        except Exception as e:
            logger.error(f"Error generating plot for '{column}': {e}")

    def query_data(self, column, value):
        if self.data.empty:
            logger.info("No data available to query.")
            return pd.DataFrame()

        if column not in self.data.columns:
            logger.error(f"Error: Column '{column}' not found in dataset.")
            return pd.DataFrame()

        try:
            result = self.data[self.data[column] == value]
            return result
        except Exception as e:
            logger.error(f"Error during query: {e}")
            return pd.DataFrame()
        
    def find_flavor(self,*args):
        result = ""
        for flavor in args:
            result = result+" "+self.data[self.data['Flavor'] == flavor]
        return result
