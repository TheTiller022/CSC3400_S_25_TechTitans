# child class of Sales (child class 2)
'''
class Sales_Calculations(Sales):
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
    

'''
import Sales.py
