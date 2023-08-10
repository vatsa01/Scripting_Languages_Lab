# Python: Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each
# element in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the
# sum of the elements of the original list as well as the new list.


from functools import reduce

# Declare a list
lst = []
print("Enter 6 Numbers:\n")
for i in range(6):
    lst.append(int(input()))
print(lst)
# Make list with 3*a[i]
lst2 = [(lambda a: 3 * a)(y) for y in lst]
print(lst2)
# Sum of list using lambda and reduce
print(reduce(lambda a, b: a + b, lst))
print(reduce(lambda a, b: a + b, lst2))
