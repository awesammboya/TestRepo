#!/usr/bin/python
# Using range function to generate numbers
# Use for loop to iterate through the numbers produced in the range then print them.

for num in range(10):
	print(num)

# print the sum of a range of numbers.
# Use for loop to iterate though the range.
# Set the sum variable to zero. Use the step value of 7

sum = 0
for i in range(2, 22, 2):
	sum = sum + i
print(sum)

# Find the square of each number in the list
numbers = [2, 23, 11, 24, 45, 67, 567, 89, 99]
#I iterateover each element and find the square.
for i in numbers:
	# ** exponent  operator
	square = i ** 2
	print("The square of: ", i, "is:", square)

