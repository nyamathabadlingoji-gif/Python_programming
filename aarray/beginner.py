# Find the largest element in an array.
arr = [22,45,7,89]
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print(largest)


# Find the Smallest Element in an Array
arr = [12,6,8,65,7]
smallest = arr[0]
for num in arr:
    if num < smallest:
        smallest = num
print(smallest)

# Find the Second Largest Element
arr = [55,65,23,87,12]
largest = second = arr[0]
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
         second = num
print(second)


# Find the Second Smallest Element
arr = [54,23,65,89,22]
smallest = second = arr[0]
for num in arr:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num != smallest:
        second = num
print(second)


# Calculate the sum of all elements.
arr = [54,23,65,89,22]
sum = 0 
for num in arr:
    sum = sum + num
print(sum)

# Calculate the average of array elements
arr = [54,23,65,89,22]
no_of_elm = len(arr)
sum = 0 
for num in arr:
    sum = sum + num
print(sum/no_of_elm)

# Count the number of even and odd numbers.
arr =[2,5,6,65,8,77,4,23,33,7]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)



