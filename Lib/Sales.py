#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
Sales = 'Lib/Sales'
'''
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
Notes:
    Applying the templete
'''
#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
#custom imports
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
# Lib/Sales.py

class Sales:
    def __init__(self, pickle_path='Input/data.pkl'):
        try:
            df = pd.read_csv('Input/data.csv')
            df.columns = df.columns.str.strip()
            os.makedirs(os.path.dirname(pickle_path), exist_ok=True)
            df.to_pickle(pickle_path)
            self.data = pd.read_pickle(pickle_path)
            self.config = {
                'columns_to_plot': ['Flavor', 'Size', 'Topping', 'Price'],
                'output_dir': 'output'
            }
            os.makedirs(self.config['output_dir'], exist_ok=True)
            logger.info(f"Data loaded from {pickle_path}")
        except Exception as e:
            logger.error(f"Failed to load pickle file: {e}")
            self.data = pd.DataFrame()

    def visualize_column(self, column):
        #print(f'config: {self.config}')
        if column not in self.config['columns_to_plot']:
            logger.error(f"Column '{column}' not found.")
            return

        output_file = f"{self.config['output_dir']}/{column.lower()}_distribution.png"
        try:
            plt.figure(figsize=(8, 5))

            if self.data[column].dtype == 'object':
                counts = self.data[column].value_counts()
                counts.plot(kind='bar', color='skyblue')
                plt.ylabel('Count')
            else:
                self.data[column].plot(kind='hist', bins=10, edgecolor='black')
                plt.ylabel('Frequency')

            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(output_file)
            plt.close()
            logger.info(f"Saved: {output_file}")
        except Exception as e:
            logger.error(f"Error generating plot for {column}: {e}")
    
    def basic_stats(self, column):
        if column not in self.config['columns_to_plot']:
            logger.error(f"Column '{column}' not found.")
            return None
        else:
            return {
                'mean': self.data[column].mean(),
                'median': self.data[column].median(),
                'std': self.data[column].std()
            }

    def position_vector(self, column):
        return self.data[column].values

    def unit_vector(self, vector):
        norm = np.linalg.norm(vector)
        return vector / norm if norm != 0 else vector

    def dot_product(self, a, b):
        return np.dot(a, b)

    def projection_vector(self, a, b):
        return (np.dot(a, b) / np.dot(b, b)) * b

    def check_orthogonality(self, a, b):
        return np.isclose(np.dot(a, b), 0)
    
    def total_sales(self):
        my_lambda = lambda a, b: a + b
        total = 0
        for row in self.data['Price']:
            total = my_lambda(total, row)
        return total
        