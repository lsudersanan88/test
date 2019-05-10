"""
Exercise 8
1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float
2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 kwargss.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 kwargss.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument
"""
import sys
import argparse

def compute(**kwargs):
   input = kwargs['input']
   if type(input) is list:
        input = list(map(int, input))
        if kwargs['action']=='sum':
            if kwargs['return_float']==True:
                return (float(sum(input)))
            if kwargs['return_float']==False:
                return (sum(input))
        if kwargs['action']=='mean':
            if kwargs['return_float']==True:
                return float(sum(input)) / max(len(input), 1)       
            if kwargs['return_float']==False:
                return int((sum(input)) / max(len(input),1))
   else:
        return "Not a List"
   

   return 

print(compute(input="[1,2,3]",action='sum',return_float=True))
print(compute(input=["5","5","5"],action='sum',return_float=False))
print(compute(input=[1,2,3],action='sum',return_float=True))
print(compute(input=[1,2,3],action='sum',return_float=False))
print(compute(input=[1,2,3],action='mean',return_float=True))
print(compute(input=[1,2,3],action='mean',return_float=False))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process integers')
    parser.add_argument('-m', '--multiply', help='Mention -m for multiplication ', type=int)
    parser.add_argument('-s', '--sum', help='Mention -s for addition', action='store_true')
    parser.add_argument('remainder', help='Provide integers to perform operation on', nargs=argparse.REMAINDER)
    

    try:
        args = parser.parse_args()

        if args.sum:
            print(sum(int(x) for x in args.remainder))
        if args.multiply:
            results = [int(i)*args.multiply for i in args.remainder]
            for row in results:
                print(row)
      
    except:
        parser.print_help()
        sys.exit(1)
