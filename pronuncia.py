import re

f = open("pronuncia.txt", encoding="utf8")
try:
    original = f.read()
finally:
    f.close()

original = re.sub(r"([abcdefghijklmnopstuvwxyzABCDEFGHIJKLMNOPSTUVWXYZàáôóêéíúüãõÀÁÔÓÊÉÍÚÜÃÕ])([Rr][aeiouàáôóêéíúüãõ])", r"\1<strong>\2</strong>", original)
original = re.sub(r"([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])(<strong>)", r"<strong>\1", original)
original = re.sub(r"\n\n", r"\n", original)
original = re.sub(r" \.", r".", original)
original = re.sub(r" ,", r",", original)

splited = original.split("\n")

textoFinal = ""

for t in splited:
    textoFinal += f"<p>{t}</p>"

print(textoFinal)

f = open("pronuncia.html", "w+", encoding="utf8")
try:
    f.write(f"<html><body>{textoFinal}</body></html>")
finally:
    f.close()
