# Python File Handling & List Comprehension: Write a python program to read the contents of a
# file (filename as argument) and store the number of occurrences of each word in a dictionary.
# Display the top 10 words with most number of occurrences in descending order. Store the length of
# each of these words in a list and display the list. Write a one-line reduce function to get the average
# length and one-line list comprehension to display squares of all odd numbers and display both.


from collections import Counter
from functools import reduce


def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())


d = word_count("lose_yourself.txt")
print(d)
# print(type(d))
lis = list(d.items())
# print(lis)
lis.sort(reverse=True, key=lambda x: x[1])
print(lis)
print("\nThe top 10 most occurred words are:")
lis2 = []
for i in range(10):
    print(lis[i][0], "\n")
    lis2.append(len(lis[i][0]))
print(lis2)
avg = (reduce(lambda a, b: a + b, lis2)) / len(lis2)
print("Average is :", avg)
lis2 = [x * x for x in lis2 if x % 2 != 0]
print("Final list = ", lis2)
