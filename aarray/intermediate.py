# Rotate an array by K positions.
arr = [1, 2, 3, 4, 5]
k = 2
k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)

# Move All Zeros to the End
arr = [0, 1, 0, 3, 12]
result = []
for num in arr:
    if num != 0:
        result.append(num)
while len(result) < len(arr):
    result.append(0)
print(result)


# Find the Missing Number (1 to N)
arr = [1, 2, 4, 5]
n = 5
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
missing = expected_sum - actual_sum
print(missing)


# Find the Duplicate Element

arr = [1, 3, 4, 2, 2]
seen = set()
for num in arr:
    if num in seen:
        print(num)
        break
    seen.add(num)

# Find All Pairs with a Given Sum
arr = [1, 5, 7, -1, 5]
target = 6
seen = set()
for num in arr:
    if target - num in seen:
        print((target - num, num))
    seen.add(num)