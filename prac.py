import sys

#return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2])
print(low,high)

def divide(a,b):
    if b==0:
        return None
    return a/b
r=divide(a=70,b=7)
print(r, file=sys.stdout)    

#wrong
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

#correct
def add_item(item,basket=None):
    if basket is None:
        basket=[]
        basket.append(item)
    return basket
print(add_item("apple"))
print(add_item("banana"))

