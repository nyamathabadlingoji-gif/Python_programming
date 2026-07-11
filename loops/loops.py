
# multiplication of the number using loop
num = int(input())
for i in range(1,11):
    print(num,"*", "=" ,num * i)


# all the odd numbers form 50 and 100
for i in range(50,101):
    if i % 2 != 0:
        print(i)

# Count how many factors a number has
num = int(input())
count = 0
for i in range(1,num + 1):
    if num % i == 0:
        count += 1
print( "number of factors=",count)