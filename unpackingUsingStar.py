#!/bin/python3
#This function will take name and number of marks
#Note that when you are using  * operator for unpacking the data ,the data must be a tuples/list that is must be iterablbe object
import math 
def avg_grades(grades):
    name, *marks=grades;
    print ("Student :"+name+" has got sum of ",math.fsum(marks));
    print("Marks ",marks); # One important thing to note that marks will be always a list.
avg_grades(["Avinash",65,75,78,98,94]);# as list
avg_grades(("Avinash",65,75,78,98,94));# as a tuple