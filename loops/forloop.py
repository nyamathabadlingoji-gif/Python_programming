# numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
    print(i)

# all even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)
\
# all odd numbers from 1 to 20.
for i in range(1,20,2):
    print(i)

# multiplication table of 7.
for i in range(7,71,7):
    print(i)

# sum of numbers from 1 to 100.
total = 0
for i in range(1,100):
    total += i
print(total)

# character in the string "Python".
ch ="python"
for i in ch:
    print(i)

# how many numbers are in the list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in numbers:
    count += 1
    print(count)

# Print every item in the list:
num = ["apple","banana","cherry"]
for i in num:
    print(i)

# Count how many even numbers are in:
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        count += 1
print(count)

# # Find the largest number in:
num = [45,87,22,65,32]
largest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
print(largest)


# Find the smallest number in:
num = [45,87,22,65,32]
smallest = num[0]
for i in range(len(num)):
    if num[i] < smallest:
        smallest = num[i]
print(smallest)

# Calculate the average of:
num = [54,84,55,59,55]
total = 0
for i in range(len(num)):
    total += num[i]
average = total / len(num)
print(average)