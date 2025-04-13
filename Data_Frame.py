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

import os
import pandas as pd
import matplotlib.pyplot as plt

#other imports

#%% USER INTERFACE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONSTANTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% CONFIGURATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% INITIALIZATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#%% DECLARATIONS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here

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
            self.data.columns = self.data.columns.str.strip()  # clean up column names
        except FileNotFoundError:
            print("Error: 'Input/data.csv' not found.")
            self.data = pd.DataFrame()
        except pd.errors.EmptyDataError:
            print("Error: 'Input/data.csv' is empty or unreadable.")
            self.data = pd.DataFrame()
        except Exception as e:
            print(f"Unexpected error loading CSV: {e}")
            self.data = pd.DataFrame()

        os.makedirs('output', exist_ok=True)

    def visualize_column(self, column):
        """Visualize and save a plot for the given column based on its type."""
        if self.data.empty:
            print("No data available to visualize.")
            return

        if column not in self.data.columns:
            print(f"Error: Column '{column}' not found in dataset.")
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
            print(f"Plot for '{column}' saved to {plot_path}")

        except Exception as e:
            print(f"Error generating plot for '{column}': {e}")

    def query_data(self, column, value):
        """Return rows where a column matches a value."""
        if self.data.empty:
            print("No data available to query.")
            return pd.DataFrame()

        if column not in self.data.columns:
            print(f"Error: Column '{column}' not found in dataset.")
            return pd.DataFrame()

        try:
            result = self.data[self.data[column] == value]
            return result
        except Exception as e:
            print(f"Error during query: {e}")
            return pd.DataFrame()


            

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

