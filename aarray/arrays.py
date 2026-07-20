# Count occurrences of a specific number.

arr = [21,22,3,65,995]
x = 4
count = 0 
for i in arr:
    if i == x:
        count += 1
print("occurrenece:0",count)


# Find the frequency of each element.
arr = [65,84,64,62,45,8]
n = len(arr)
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    count = 1
    for j in range(i + 1,n):
        if arr[i] == arr[j]:
            count += 1
            visited[j] = True
    print(arr[i], "->",count)


#  Find Average
arr = [10,20,30,55]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
average = sum / len(arr)
print(average)


# Count Positive, Negative and Zero
arr = [1,-3,0,2,-8,6]
positive = negative = zero = 0
for i in range(len(arr)):
    if arr[i] > 0:
        positive += 1
    elif arr[i] < 0:
        negative += 1
    else:
        zero += 1
print("positive =",positive)
print("negative =",negative)
print("zero =",zero)

# find max and min 
arr = [10,20,30,35,40]
max = arr[0]
min = arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print("maximum =",max)
print("minimum =",min)

# Linear Search
arr = [10,20,30,40,50]

key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not Found")