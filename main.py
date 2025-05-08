#Version: v0.1
#Date Last Updated: 4-7-2025

#%% MODULE BEGINS
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
from Lib.Sales_Calculation import Sales_Calculation

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
# Version: v0.1
# Date Last Updated: 4-7-2025

#%% MODULE BEGINS
'''
Version: v0.1
Description:
    main calls information from input and libraries and thus needs to be imported.
Authors:
    Tyler Poirrier, Brandon Stromeyer
Date Created : 4-7-2025
Date Last Updated: 4-7-2025
'''

#%% IMPORTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% MAIN FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    d.visualize_violin('Price')
    d.visualize_boxplot('Size')
    d.visualize_scatterplot('Flavor', 'Price', 'Size')

    s = Sales_Calculation()

    columns = ['Flavor', 'Size', 'Topping', 'Price']
    for col in columns:
        print(f"Generating distribution plot for {col}...")
        s.visualize_column(col)

    
    print("\nBasic Statistics for 'Price':")
    stats = s.basic_stats('Price')
    for stat_name, stat_value in stats.items():
        print(f"{stat_name.capitalize()}: {stat_value:.2f}")
    
    
    print("\nVector Operations on 'Price':")
    price_vector = s.position_vector('Price')
    unit_vec = s.unit_vector(price_vector)
    dot = s.dot_product(price_vector, unit_vec)
    ortho = s.check_orthogonality(price_vector, unit_vec)

    print(f"First 5 of position vector: {price_vector[:5]}")
    print(f"First 5 of unit vector: {unit_vec[:5]}")
    print(f"Dot product: {dot:.2f}")
    print(f"Orthogonality check: {ortho}")

    print("\nJoint Counts (Flavor vs Size):")
    joint_counts_df = s.joint_counts('Flavor', 'Size')
    print(joint_counts_df)
    joint_counts_df.to_csv('output/JointCounts_Flavor_Size.csv', index=True)
    s.plot_stacked_bar('Size', 'Flavor')

    print("\nJoint Probabilities (Flavor vs Size):")
    joint_probs_df = s.joint_probabilities('Flavor', 'Size')
    print(joint_probs_df)
    joint_probs_df.to_csv('output/JointProbs_Flavor_Size.csv', index=True)

    print("\nConditional Probabilities (Flavor given Size):")
    cond_probs_df = s.conditional_probabilities('Size', 'Flavor')
    print(cond_probs_df)
    cond_probs_df.to_csv('output/ConditionalProbs_Flavor_given_Size.csv', index=True)
    s.plot_stacked_bar('Size', 'Flavor')

    print("\nPermutations of Topping (r=2):")
    perms = s.generate_permutations('Topping', r=2)
    print(perms[:5])  

    print("\nCombinations of Topping (r=2):")
    combs = s.generate_combinations('Topping', r=2)
    print(combs[:5])  
    

#
#%% SELF-RUN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Main Self-run block
if __name__ == "__main__":
    #print(f"\"{module_name_gl}\" module begins.")
    main()
