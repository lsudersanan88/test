#                       LIST COMPREHENSION

# return all number less than 10
def print_num():
    return [num  for num in range(10)]
# print(print_num())

# return all odd number less than x
def odd_num(x):
    return [num  for num in range(x) if num % 2 != 0]
# print(odd_num(10))

# Return a list, where every element in my_list that is greater than the max_value, is reduced to max_value.
#     EX: ceiling([1, 10, 100, 200, 300], 150) -> [1, 10, 100, 150, 150]
def ceiling(my_list, max_value):
    return [num if num < max_value else max_value for num in my_list]
# print(ceiling([1, 10, 100, 200, 300], 150))

# Return a list, where every element in my_list that is less than min_value is raised to min_value, AND
#      every element that is greater than max_value is reduced to max_value.
#     EX: squish([1, 10, 100, 200, 300], 15, 150) -> [15, 15, 100, 150, 150]
def squish(my_list, min_value, max_value):
    return [min_value if num < min_value else (max_value if num > max_value else num)  for num in my_list]
# print(squish([1, 10, 100, 200, 300], 15, 150))


#                       SET COMPREHENSION {}

def example_set(my_list):
    return {s for s in my_list }
# print(example_set([1,2,3,2]))

#                       Dictionary comprehension {}

def dict_low_pass(my_dict):
    """
    Return a dictionary of only the key/value pairs from my_dict whose value is GREATER THAN 10.
    EX: dict_low_pass({'a': 1, 'b': 10, 'c': 11}) -> {'c': 11}
    """
    return {key : my_dict[key]  for key in my_dict if my_dict[key] > 10}
# print(dict_low_pass({'a': 1, 'b': 10, 'c': 11,'d': 12, 'e': 21}))

def dict_example(my_dict, min_value, max_value):
    return {key : max_value  if my_dict[key] > max_value else (min_value if my_dict[key] < min_value else my_dict[key])for key in my_dict}

print(dict_example({'a': 15, 'b': 1, 'c': 7,'d': 11, 'e': 21}, 10, 12))
