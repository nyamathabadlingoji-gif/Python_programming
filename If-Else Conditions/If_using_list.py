# Create a list of your favorite fruits. Check if "apple" is in the list.
favorite_fruits = ["banana", "orange", "grape", "mango",]
if "apple" in favorite_fruits:
    print("You really like apple!")
else:
    print("apple is not in my favorite fruits list")

# Create a shopping list containing 5 items.
shopping_list =["milk","sugar","bread","powerd","salt"]
if "milk"in shopping_list:
    print("buy milk")
else:
    print("milk is not needed ")

# student marks and grade
# 3. Student Marks

# Create a list containing marks of five students.
marks = [99,9, 78,96,88]
if marks[0] >= 90:
    print("Grade A")
elif marks[0] >= 80:
    print("grade B")
elif marks[0] >=70:
    print("grade C")
else:
    print("grade D")



# Create a list of numbers.
numbers = [10, 20, 30, 40, 50]
if len(numbers) > 5:
    print("large list")
else:
    print("small list")


# Create a list of numbers.
numbers = [10, 20, 30, 40, 50]
if numbers[0] % 2 == 0:
    print("even number")
else:
    print("odd number")

# Find the Largest Number
numbers = [10, 20, 30, 40, 50]
if max(numbers) == 50:
    print("The largest number is 50")   
elif max(numbers) == 40:
    print("The largest number is 40")
else:
    print("The largest number is not 50 or 40")