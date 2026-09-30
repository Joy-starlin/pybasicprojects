#*args and **kwargs are used to pass a variable number of arguments to a function.

#args are used with a single data types though they return a tuple
#hold positional arguments
def total(*args):
    print(type(args))
    print(sum(args))
total(12, 13,14, 80)

#**kwargs return a dictionary and are used with different data types
#hold keyword arguments
def create_profile(**kwargs):
    print(type(kwargs))
    print(kwargs)
create_profile(name="Karen Joy", age=22, city="Kampala", country="Uganda")
