# Print numbers from 1 to 10.
i = 1
while i <= 10:
    print(i)
    i += 1


# Print numbers from 1 to 10.
i = 10
while i >= 1:
    print(i)
    i -= 1

#   Print all even numbers from 1 to 100
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1



# Print all odd numbers from 1 to 100
i = 1 
while i <=100:
    if i % 2 != 0:
        print(i)
    i += 1

# Print all multiples of 5 from 1 to 100
i = 5 
while i <= 100:
    print(i)
    i += 5

# Print the multiplication table of a given number
num = int(input())
i = 1 
while i <= 100:
    print(num, "*", i, "=",num * i)
    i += 1

# Find the sum of numbers from 1 to N
num = int(input("enter N: "))
i = 1 
sum = 0
while i <= n:
    sum += i
    i += 1
print("sum =",sum)

# Find the sum of even numbers from 1 to N
n =  int(input())
i = 2
sum = 0
while i <= n:
    sum += i
    i += 2
print("sum of even numbers = ",sum)

# Find the sum of odd numbers from 1 to N
n =  int(input())
i = 1
sum = 0
while i <= n:
    sum += i
    i += 2
print("sum of even numbers = ",sum)

