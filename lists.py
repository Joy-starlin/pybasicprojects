#Lists are an ordered data structure, mutable and can hold any datatype. 
# They are defined using square brackets [] and can be indexed and sliced.

colors = ["red", "green", "blue", "yellow"]
print(colors)

#adding elements
colors[0] = "orange"  # changing the first element
print(colors)

colors.insert(1, "red")  # inserting an element at index 1
print(colors)

colors.extend(["green", "blue"])  # adding multiple elements to the end
print(colors)


colors.append("purple")  # adding an element to the end
print(colors)

colors.insert(2, "pink")  # inserting an element at index 2
print(colors)

#removing elements
colors.remove("green")  # removing an element by value
print(colors)

del colors[1]  # removing an element by index
print(colors)

colors.pop()  # removing the last element
print(colors)

#colors.clear()   removes all elements

#slicing
print(colors[1:3])  # slicing from index 1 to 2 
print(colors[:3])  # slicing from the start to index 2
print(colors[2:])  # slicing from index 2 to the end

#negative slicing
print(colors[-3:])  # slicing the last 3 elements
print(colors[-3:-1])  # slicing from the third-to-last to the second-to-last element    