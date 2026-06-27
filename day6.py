#  using a for loop to print numberes
for i in range(1,20):
    print(i)

 printin a numbers 1 to one million using a for loop
for i in range(1,100001):
    print(i)


# using the min()and max() and sum()
Create a list of numbers from 1 to 1,000,000
numbers = list(range(1, 100))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

#  print odd numbers using loop
odd_numbers =list(range(1,21,2))
for i in odd_numbers:
    print(i)

#  printing a multiple of 3 from 3 to 30
multiple = list(range(3,30,3))
for i in multiple:
    print(i)

# printing first 10 cubes
cubes =[]
for i in range(1,11):
    cubes.append(i ** 3)
for cube in cubes:
    print(cube)


#  first 10 cubes 
Generate a list of the first 10 cubes
cubes = [i ** 3 for i in range(1, 11)]

print(cubes)