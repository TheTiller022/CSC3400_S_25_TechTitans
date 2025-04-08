# Child class of Frequency (child class 1)
'''
class Dataframe(Frequency):
  this child class of the parent class "frequency", will read from the input .....csv file that stores all of our order information
    - the orders are broken into columns with size, flavor, toppings, and price
    - the rows are the order numbers themselves

  to vizualize the data using violin plots, whisker-box plots, and scatter plots, the data from each column will be broken up and compare between the rows
    - since there is a variety of ways the compare orders, we can look at individual elements, or combination of elements to compare using different plots

  to query the data for search and display, we can set multiple conditions to compare each rows
    - such as if a snowball is a size "L" and flavor "tiger blood"
    - this is done by using & or || expressions to ensure that we are setting the data to be compared by more than one condition
      - this can set each row value to true or false depending on this boolean expression
'''
import Frequency
