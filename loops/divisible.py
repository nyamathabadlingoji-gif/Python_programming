# numbers divisible by both 3 and 5 from 1 to 100.
numbers = []
for i in range(1,100):
    if i % 3 == 0 and i % 5 ==0:
        numbers.append(i)
print(numbers)

# square of each number from 1 to 10.
numbers = [i**2 for i in range(1,11)]
print(numbers)

# cube of each number from 1 to 10.
numbers =[]
for i in range(1,11):
    numbers.append(i**3)
print(numbers)

# Reverse a list using a loop
numbers = [1,2,3,4,5]
for i in numbers[::-1]:
    print(i)

# count vowels in a string using a loop
text = "Artificial Intelligence" 
vowels = "aeiouAEIOU"
count =  0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)


# 1. Print
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print("*" * i)


# print
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    print("*" * i)

# 3. Print
# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

# 4. Print
# 11111
# 22222
# 33333
# 44444
# 55555
for i in range(1, 6):
    for j in range(5):
        print(i, end="")
    print()

# 5. Print Multiplication Tables from 1 to 5
for i in range(1, 6):
    print(f"Multiplication Table of {i}")

    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

    print()