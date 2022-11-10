f = open("text.txt", "r")
i = ["a", "e", "i", "o", "u", "y"]
b = f.read()
print(b)
for y in b:
    for z in i:
        if z == y:
            if z == "a":
                c1 = b.count("a")
            elif z == "e":
                c2 = b.count("e")
            elif z == "i":
                c3 = b.count("i")
            elif z == "o":
                c4 = b.count("o")
            elif z == "u":
                c5 = b.count("u")
            elif z == "y":
                c6 = b.count("y")
print("number of  A :", c1)
print("number of  E :", c2)
print("number of  I :", c3)
print("number of  O :", c4)
print("number of  U :", c5)
print("number of  Y :", c6)