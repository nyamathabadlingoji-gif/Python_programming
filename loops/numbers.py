# all prime numbers between 1 and 100
for num in range(2, 101):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# the sum of all prime numbers from 1 to N
n = int(input())
prime_sum = 0
for num in range(2, n + 1):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num
print("sum of prime numbers",prime_sum)



# number of digits in an integer without using len()
def count_digits(number):

   if number == 0:
    return 1
    number = abs (number)
    count = 0
    while number > 0:
         number = number // 10
    count += 1
    return count
print(count_digits(61656626))

# Reverse an integer using a loop
num = int(input())
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse *10 + digit
    num = num // 10
print("reversed number:",reverse)


for i in range(20,10,-1):
    print(i)

# whether a number is a palindrome
num = int(input())
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse *10 + digit 
    num = num // 10
if original == reverse:
   print("palindrome")
else:
   print("not a palindorme")


