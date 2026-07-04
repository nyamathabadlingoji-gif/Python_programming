# examples problems
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points!")


# fails the test using if statement
alien_colour = "red"
if alien_colour == "green":
    print("the player just earned 5 points!")

# uses elif statement for the test 
elif alien_colour == "yellow":
    print("the player just earned 10 points!")
else:
    print("the player just earned 15 points!")


# uses else statement for the test
alien_colour = "red"
if alien_colour == "green":
    print("the player just earned 5 points!")
else:
    print("the player just earned 15 points!")


# uses if and elif and else statements for the test
alien_colour = "yellow"
if alien_colour == "green":
    print("the player just earned 5 points !")
elif alien_colour == "yellow":
    print("the player just earned 10points")
else:
    print("the player just earned 15points")