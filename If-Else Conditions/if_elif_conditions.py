# whether a number is a three-digit number.
number = 17
if 100 <= number <= 999:
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")


# whether a character is uppercase or lowercase.
ch = input("lingan:")
if ch.isupper():
    print(ch, "is uppercase")
else:
    print(ch, "is not uppercase")

# character is an alphabet, digit, or special character.
ch = input("enter a character:")
if ch.isalpha():
    print(ch,"is an alphabet")
elif ch .isdigit():
    print(ch,"is a digit")
else:
    print(ch,"is a special character")


# electricity bill based on slab rates.
units = int(input("enter the number of units consumed :"))
if units <=100:
    bill = units * 5
    print("The electricity bill is:", bill)

# income tax based on salary slabs.
salary = int(input("enter your salary :"))
if salary <= 50000:
    tax = salary * 0.1
    print("The income tax is:", tax)
elif salary <= 100000:
    tax = salary * 0.2
    print("The income tax is:", tax)
else:
    tax = salary * 0.3
    print("The income tax is:", tax)

# grade of a student based on marks.
marks = int(input("enter your marks :"))
if marks >= 90:
    print("grade is A")
elif marks >= 80:
    print("grade is B")
else:
    print("grade is C")


# whether a triangle is valid.
a = int(input("enter the first side of triangle :"))
b = int(input("enter the second side of the triangle:"))
c = int(input("enter the third side of the triangle:"))
if a + b > c and b + c > a and c + a > b:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")


# the type of triangle (Equilateral, Isosceles, Scalene
if a == b == c:
    print("The triangle is Equilateral.")
elif a == b or b == c or c == a:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")