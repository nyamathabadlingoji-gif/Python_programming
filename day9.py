# # #  can create their list by copying
# # my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:" )
print(my_foods)
print("\nmy freinds favporite foods are:")
print(friend_foods)


# slicing
pizzas = ["Pepperoni", "Cheese", "Veggie", "BBQ Chicken", "Margherita", "Paneer"]

print("The first three items in the list are:")
print(pizzas[:3])

print("\nThree items from the middle of the list are:")
print(pizzas[2:5])

print("\nThe last three items in the list are:")
print(pizzas[-3:])

# pizza
my_pizzas = ['chicken','veg','panier']
friend_pizzas = my_pizzas[:] 
my_pizzas.append('butter')
friend_pizzas.append('chiees')
print("my favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizzas in friend_pizzas:
    print(pizzas)