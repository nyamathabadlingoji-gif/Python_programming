# reverse a string without using[::-1]

str = "lingan"
reverse = "" 
for char in str:

    reverse = char + reverse
print(reverse)

#  check if two strings are Anagrams
str1 = "lingan"
str2 = "ganlin"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("not anagram")


# find the longest word in a sentence
str = "my name is lingoji"
words = str.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

# Count the Frequency of Each Character
str = "lingannnnnnnnnnn"
frequency = {}
for char in str:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char] = 1
for key,value in frequency.items():
    print(key,":",value)

# Find the First Non-Repeating Character
str = "lingannnnnnnnnnn"
frequency = {}
for char in str:
    
    frequency[char] = frequency.get(char,0) + 1
for char in str:
   if frequency[char] == 1:
      print("first non-repeating characters:",char)
      break
else:
   print("no non-repeating character")


# Find the First Repeating Character
str = "swiss"
visited = set()
for char in str:
   if char in visited:
      print("first repeating character:",char)
      break
   visited.add(char)
else:
   print("no reparting character")

#Remove Duplicate Characters While Preserving Order
string = input("Enter a string: ")

result = ""
visited = set()

for char in string:
    if char not in visited:
        result += char
        visited.add(char)

print(result)

# Check if a String is a Palindrome Without Using Reverse Functions
string = input("Enter a string: ")

left = 0
right = len(string) - 1

is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")