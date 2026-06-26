# lists in python with all methods
places = ["Japan", "Switzerland", "Australia", "Canada", "Italy"]

# Original list
print("Original list:")
print(places)

# Print list in alphabetical order without changing the original list
print("\nAlphabetical order:")
print(sorted(places))

#  original list is unchanged
print("\nOriginal list after sorted():")
print(places)

# 
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# original list is unchanged
print("\nOriginal list after reverse sorted():")
print(places)

# Reverse the order of the list
places.reverse()
print("\nList after reverse():")
print(places)


places.reverse()
print("\nList after second reverse():")
print(places)

# Sort list alphabetically
places.sort()
print("\nList after sort() (alphabetical):")
print(places)

# Sort list in reverse alphabetical order
places.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(places)


# using lists with the append insert methods


guests = ["ram","shyam","sita","gita"]

# Printing invation message
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Print the number of guests being invited
print(f"\nI am inviting {len(guests)} people to dinner.")




# using lists with the del and reverse and sort methods

india = ["mountains","rivers","deserts","forests"]
print(india)
# append beaches to the list
india.append("beaches")
print(india)
#  inset lakes at the third position in the list
india.insert(3,"lakes")
print(india)
#  delete the third element from the list
del india[2]
print(india)
# remove the second element from the list
india.remove("rivers")
print(india)

# reverse the order of the list
india.reverse()
print(india)

# sort the list in the alphabetical order
india.sort()
print(india)




# # printing the list by step by step 
magicians = ['alice','david','caroling']
for magician in magicians:
    print(magician)


# without using built in functions reversing the list

goa  = [1,2,3,4,5,6]
for i in goa [-1:  :-1]:
    print(i)  