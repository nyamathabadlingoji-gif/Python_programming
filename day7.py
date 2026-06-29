

# # slicing the index
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])


# #copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)  


# copying a list and appending a new values in the list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)



# Multiplication table of 5

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


 # Calculate the sum of numbers from 1 to 100

total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)


# counting the number of elements in  LIST

numbers = [10, 20, 30, 40, 50]

count = 0

for number in numbers:
    count += 1

print("Number of elements:", count)