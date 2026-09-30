#A function wrapping another function to modify it

#A function returning a function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
    return wrapper

#this is the base function where the decorator is applied to it. The decorator is applied by using the @ symbol followed by the decorator name before the function definition.
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"here is your {flavor} ice cream")

get_ice_cream("vanilla")