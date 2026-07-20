# 1. Count the frequency of each character in a string
string = "programming"
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)



# Count the frequency of each word in a sentence
string = "my name is lingoji"
words = string.split()
frequency = {}
for char in words:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

# merge two dictionarys
dict1 ={"a" : 10,"b": 20}
dict2 = {"c" : 30,"d":50}
dict1.update(dict2)
print(dict1)

# find the key of a maximum value
marks = {
    "lingoji":75,
    "chennai" : 95,
    "bheem" : 85,
    "bhanu" : 65,
    "manoj" : 75

}
key = max(marks, key=marks.get)
print(key)



# find the minimum key value
marks = {
    "lingoji":75,
    "chennai" : 95,
    "bheem" : 85,
    "bhanu" : 65,
    "manoj" : 75

}
key = min(marks, key=marks.get)
print(key)

# sum of all the values in a dictionary
numbers ={
    "a":10,
    "b":20,
    "c":30
}
total = sum(numbers.values())
print(total)