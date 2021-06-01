# References that I used to learn this:
# Harvard cs50 course - https://cs50.harvard.edu/x/2020/weeks/6/
# https://developers.google.com/edu/python/dict-files

# we can declare with values
dict1 = {"Geeks": 1, "for": 2, "geeks": 3}
print("Original dictionary is : " + str(dict1))

# or, we can declare without values, implicit
dict2 = {}

# or explicit
dict3 = dict()

# we can interate direct on a for
print("First dictionary values: ")
for i in dict1:
    print(f"key: {i} => value: {dict1[i]}")

print()
print("Second dictionary values: ")
dict2[1] = 15
for i in dict2:
    print(f"key: {i} => value: {dict2[i]}")

print()
print("Second dictionary values: ")
dict3["523"] = 453245
dict3["123"] = 7567
for i in dict3:
    print(f"key: {i} => value: {dict3[i]}")


print()
if (1 in dict2):
    print("It is also possible to check if a key is present in dictionary.")

print('or sort by keys before print')
for i in sorted(dict3.keys()):
    print(f"key: {i} => value: {dict3[i]}")

print('There is also a crazy way of formating getting values for Geeks: %(Geeks)d and For: %(for)s ' % dict1)
