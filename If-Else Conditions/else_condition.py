Hi Harini, it’s great to connect with you. Looking forward to staying in touch.”

num = int(input())
for i in range(1,num+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"divisible by 3 and 5",i)
    else:
        print("no",i)

check whether a number is a multiple of 7.
num = 7
# for i in range(1,num+1):
if num % 7 == 0:
    print(num, "is a multiple of 7")
else:
    print(num,"is not a multiple")


# to check if a student has passed (marks ≥ 35)
marks = 86
if marks >= 35:
    print(marks,"have passed")
else:
    print(marks,"not passed")  

# program to find the largest of three numbers.

num1 = 14
num2 = 18
num3 = 90
if num1 >= num2 and num1 >= num3:
    print(num1,"is the largest number")
elif num2 >= num1 and num2 >= num3:
    print(num2,"is the largets number")
else:
    print(num3,"is the greatest number") 

# program to find the smallest of three numbers.
num1 = 12
num2 = 22
num3 = 95
if num1 < num2 and num1 < num2:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

# to check whether a character is uppercase or lowercase.
