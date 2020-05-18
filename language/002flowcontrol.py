# References that I used to learn this:
# Harvard cs50 course - https://cs50.harvard.edu/x/2020/weeks/6/

if True:
    print("Bool is aways Captalize in python True or False, or don't even compile")

if 1 == 1:
    print('Uses == to compare things')

if True or False:
    print("Uses 'or' instead of && ")

if 1 in [0, 1, 2, 3]:
    print("accept list")

print()

print("interate in list naturally")
for i in [0, 1, 2]:
    print(f"{i} ", end="")

print()

print("or like a normal for")
for i in range(5):
    print(f"{i} ", end="")
print("range() is exacly lika a array" + str(range(5)))

print()

print("or like in a while")
i = 0
while i < 5:
    print(f"{i} ", end="")
    i += 1
