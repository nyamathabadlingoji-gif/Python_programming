
# Print each fruit in the list:
fruits = ["apple","banana","mango","orange"]
for i in fruits:
    print( 'I like ' + (i))

# list of the squares of numbers from 1 to 10.
squares = []
for i in range (1,11):
    squares.append(i ** 2)
print(squares)

# list of the cubes of numbers from 1 to 10.
cubes = []
for i in range(1,11):
    cubes.append(i ** 3)
print(cubes)

# Print each element along with its index.
fruits =["apple","banana","mango","orange"]
for index, fruits in enumerate(fruits):
    print(index,fruits)


# Python program to count how many even and odd numbers are in a list.
numbers = [10, 15, 22, 33, 40, 51, 62, 75]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# the sum of all even numbers in a list.
numbers = [ 10,15,12,14,7,89,85,56,33]
even_sum = 0
for number in numbers:
    if number  % 2 == 0:
        even_sum += number
print("Sum of even nubers:",even_sum)

# Reverse a list using a for loop
list =[ 10,15,14,87,6]
reversed_list = []
for i in range(len(numbers) -1,-1,-1):
    reversed_list.append(numbers[i])
print(reversed_list)