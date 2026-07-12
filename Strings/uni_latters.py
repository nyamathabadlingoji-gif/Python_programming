# reversed string
string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

print("Reversed String:", reverse)

# the Length of a String Without Using len()
str = "python"
count = 0
for ch in str:
    count += 1
print("length =",count)


# Count the Number of Vowels
str = "lingan"
count = 0 
for ch in str:
    if ch in "aeiou":
        count += 1
print(count)

# Count the Number of Consonants
str = "programming"
count = 0
for ch in str:
    if('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        if ch not in "aeiouAEIOU":
            count += 1
print("number of consonants =",count)

# Count Digits and Special Characters
str = "python@123"
digits = 0
special = 0
for ch in str:
    if '0' <= ch <= '9':
        digits += 1
    elif not(('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
        special += 1
print("digits =",digits)
print("special characters =", special)

# Check Whether a String is a Palindrome
str = "hello"
reverse ="" 
for ch in str:
    reverse = ch + reverse
if str == reverse:
    print("palindrome")
else:
    print("not palindrome")


# Convert Lowercase to Uppercase (Without upper())
str = "python"
result = "" 
for ch in str:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch)- 32)
    else:
        result += ch
print(result)

#  convert lowercase to uppercase(without lower())
str = "PYTHON"
result = ""
for ch in str:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch)+ 32)
    else:
        result += ch
print(result)

# Toggle the Case of Every Character (Without swapcase())
str = "Python"
result = "" 
for ch in str:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch)+32)
    elif 'a' <= ch <= 'z':
        result += chr(ord(ch)-32)
    else:
        result +=ch
print(result)