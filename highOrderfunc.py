#high order functions

#map applies a func to each item
nums=[1,2,3,4,5,6,7]
square=list(map(lambda x:x**2,nums))
print(square)

#filter returns items where only the function is true
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

#functools
#instead of map and filter list comprehensions and generator expressions

from functools import reduce
product=reduce(lambda a,b: a*b, nums)
print(product)
squares=[x**2 for x in nums]
even=[x for x in nums if x%2==0]
print(f"square={squares}, even={even}")