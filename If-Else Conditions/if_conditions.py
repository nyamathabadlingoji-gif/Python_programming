# whether a number is even or odd.
i = int(input())
if i % 2 == 0:
    print("even number")
else:
    print("odd number")

# a person is eligible to vote (age ≥ 18).
age = int(input())
if age >= 18:
   print("you are aligible to vote:")
else:
    print("you r not elegible for vote")

# find the greater of two number
num1 = int(input())
num2 = int(input())
if  num1 > num2:
    print(num1,"is greater")
elif num2 > num1:
    print(num2,"is greater")
else:
    print ("both numbers r equal")

# Check whether a year is a leap year
year = int(input())
if(year % 400 == 0):
   
   print("leap year")
else:
    print("not a leap year" )
# Check whether a number is divisible by 5
num = int(input())
if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")


# Check whether a character is a vowel or a consonant

ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")