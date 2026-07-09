# number of consonants in a string
text = "Artifiicial Intelligence"
vowels = "aeiouAEIOU"
consonant_count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        consonant_count += 1

print("Number of consonants in the string:", consonant_count)

# Reverse a string using a loop
text = "pythone"
reversed_string = ""
for char in text:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)