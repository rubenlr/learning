
# References that I used to learn this:
# Harvard cs50 course - https://cs50.harvard.edu/x/2020/weeks/6/
# Google Python Class - https://www.youtube.com/watch?v=tKTZoB2Vjuk


# Always starts with hello world
print("Hello World")

# Print will make new lines at the end of it
print()

# Concat variables or values
print("Concat text" + " here, or using a variable like example below")
name = "Rúben Lício Reis"
print("My name using variable: " + name)
email = "rubenlr@gmail.com"
print(f"My e-mail is {email}")

print(f"Short formatting auto convert int into str {98}")
print("With variables i have to specify convertion into str " + str(98))

print()

# Removing automatic new line
print("I is possible to write a print with a specify end string. Default is \\n (scaped with backslash). In this case none:")
print("I also cold print", end="")
print(" without a new line")

print()

# Print multiply
print("It is possible to using a loop with plain and flat python syntax")
print("I'm studing python. " * 5)
