'''
1) Write a Lambda Functions that takes two arguments and return their sum
'''

sum = lambda a,b:a+b
print(sum(10,20))

'''
2)Write a Lambda Function to computer the square of a given number
'''
square = lambda a:a*a
print("value of square:",square(10))

'''
3) Use each of map, filter, and reduce to fix the broken code
'''
'''
# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
'''
my_floats = [4.35,6.09,3.25,9.77,2.16,8.88,4.59]
my_floats = list(map(lambda a:a*a,my_floats))
print("{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}".format(my_floats[0],my_floats[0],my_floats[0],my_floats[0],my_floats[0],my_floats[0],my_floats[0]))
'''
# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["Python", "Programming", "Language", "Technology", "Cloud"]
'''
my_names = ["Python","Programming","Language","Technology","Cloud"]
my_names = list(filter(lambda a:  len(a)<=7,my_names))
print(my_names)

"""
Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
"""
from functools import reduce
my_numbers = [4,6,9,23,5]
my_numbers = reduce(lambda x,y:x*y,my_numbers)
print(my_numbers)

'''
4)Write the syntax of map(), filter() and reduce()
'''

#map() syntax-> map(function,iterable)
#filter() syntax-> filter(function,iterable)
#reduce() syntax->(function,iterable,initializer = None)


'''
5)Write a Python program using the map function to identify whether each number In  a list Is even or odd
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = list(map(lambda a: 'even' if  a%2==0 else 'odd',numbers))
print(numbers)

'''
👉Write another program using the filter function to extract and print only the even numbers from the list
'''

numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers1 = list(filter(lambda a: a%2==0,numbers1))
print(numbers1)













