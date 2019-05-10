
def what_are_args(*args):
    print(args)  # try printing 'args' without the *, what changed?
    return None

# what_are_args('hi', True)


def return_odd_num(*args):
    return [num  for num in args if type(num) == int and num % 2 != 0]

# print(return_odd_num(1,2,3,4,5,'hi', True))

def my_def(*my_args):        # naming the variable 'args' is just a convention, it can be named anything, the * is whats important
    print(my_args[0:3])      # the tuple args can be subscripted (it can do everything a tuple can)

# my_def('hello', 2, [1], {'key': 'value'})

############################# KWARGS

# ## Accepting  **Kwargs
def what_are_kwargs(**kwargs):
    print(kwargs)           # {'my_kw': True, 'your_kw': 10, 'something_lines': False}
    print(type(kwargs))     # <class 'dict'>
    return

# what_are_kwargs(my_kw=True, your_kw=10, something_lines=False, kv='HI')


def return_number(**kwargs):
    return ''.join([key  for key in kwargs if type(kwargs[key]) == int])

# print(return_number(my_kw=True, your_kw=10, something_lines=False, kv='HI'))

def return_int_val_from_arg_kwarg(*args, **kwargs):
    list1 = [val for val in args if type(val) == int ]
    list2 = [kwargs[key] for key in kwargs if type(kwargs[key]) == int]

    return [list1, list2]

# print(return_int_val_from_arg_kwarg(1,2,3, True, 'Mohan', a=7, b=9, c='kv'))

# # GOOD example
def my_kwargs(**kwargs):
    my_name = kwargs.get('name', None)
    my_food = kwargs.get('food', 'Meatballs')
    print('Name is {}, Food is {}'.format(my_name, my_food))

# my_kwargs(name='Stanley', food='Pretzel')  # no issues
my_kwargs(name='Stanley')

# # BEST example
def my_kwargs(**kwargs):
    my_name = kwargs.get('name', None)
    if my_name is None:
        raise Exception('Name is required, no key word argument "name" found')

    my_food = kwargs.get('food', 'Meatballs')
    print('Name is {}, Food is {}'.format(my_name, my_food))

# my_kwargs(name='Stanley', food='Pretzel')  # no issues
# my_kwargs()                                # Exception: Name is required, no key word argument "name" found
