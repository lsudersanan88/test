"""
Exercise 9
1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math

def timing_function(some_function):
	
    def wrapper():
	
        t1 = time.time()
        some_function()
        t2 = time.time()
        sizeOfReturnValue = sys.getsizeof(some_function())
        process_time = time.process_time() 
        return "Time it took to run the function: " + str((t2 - t1)) + "\n" + "Size of the return value: "+str(sizeOfReturnValue) + "\n" +"Process Time: "+str(process_time)+ "\n"+"------------"

    return wrapper


@timing_function
def for_loop():
    num_list = []
    for num in (range(1, 1000001)):
        num_list.append(num)
    return num_list

@timing_function       
def list_comp():
	num_list = [num for num in (range(1, 1000001))]
	return num_list
	
@timing_function  
def	numpy_list():
	numpy_list = numpy.arange(1, 1000001)
	return numpy_list

@timing_function  
def	pandas_list():
	pandas_dataframe=pandas.DataFrame(numpy.arange(1, 1000001))
	return pandas_dataframe

@timing_function  
def	generator_list():
	generator_list = (num for num in (range(1, 1000001)))
	return generator_list
	

@timing_function 
def for_loop_log():
    num_list_log = []
    for num in (range(1, 1000001)):
    	num_list_log.append(math.log10(num))
    return num_list_log
        
@timing_function 
def list_com_log():
	num_list_log = [math.log10(num) for num in (range(1, 1000001))]
	return num_list_log

@timing_function 
def numpy_list_log():
	numpy_list_log = numpy.log10(numpy.arange(1, 1000001))
	return numpy_list_log

@timing_function 
def pandas_list_log():
	pandas_dataframe=pandas.DataFrame(numpy.log10(numpy.arange(1, 1000001)))
	return pandas_dataframe

@timing_function 
def generator_list_log():
	generator_list_log = (math.log10(num) for num in (range(1, 1000001)))
	return generator_list_log

print("For Loop: "+for_loop())
print("List Comprehension: "+list_comp())
print("Numpy List: "+numpy_list())
print("Pandas List: "+pandas_list())
print("Generator List: "+generator_list())

print("##################")

print("For Loop Log: "+for_loop_log())
print("List Comprehension Log: "+list_com_log())
print("Numpy List Log: "+numpy_list_log())
print("Pandas List Log: "+pandas_list_log())
print("Generator List Log: "+generator_list_log())

