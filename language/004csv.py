# References that I used to learn this:
# Harvard cs50 course - https://cs50.harvard.edu/x/2020/weeks/7/

import csv

csvFileName = 'CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv'

counts = {}

with open("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].lower()

        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

for title, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(title, count, sep=" | ")
