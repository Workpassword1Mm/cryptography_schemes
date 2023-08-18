#they produce the same result the methods and structures are what's different

first method with import
import string

Library = string.ascii_uppercase + string.digits + "_"

List = [165,248,94,346,299,73,198,221,313,137,205,87,336,110,186,69,223,213,216,216,177,138]

for items in List:

    print(Library[items%37], end="")

second method without import(easiest method)
List = [165,248,94]

for items in List:
    remainders = items%37

    if 0 <= remainders <= 25:
        print("Alphabet")
    if 26 <= remainders <= 35:
        print("Digits")
    if remainders == 36:
        print("Underscore")

third method without import
msg = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213".split()
print(msg)
mods=[i for i in range(0,37)]
print(mods)

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
print(chars)

d = {mods[i]: chars[i] for i in range(len(mods))}
print(d)

print("picoCTF{", end='')
for i in range(len(msg)):
    print(d[int(msg[i]) % 37], end='')

fourth method without import but the modular has an inverse value meaning it starts from 1 and is to the power of -1
msg = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42".split()
print(msg)
mods=[i for i in range(1,38)]
print(mods)

chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
print(chars)

d = {mods[i]: chars[i] for i in range(len(mods))}
print(d)

print("picoCTF{", end='')
for i in range(len(msg)):
    print(d[pow(int(msg[i]),-1,37)], end='')
 
#you can change the range however you would like alongside the modular as long as you have the correct calibrations for the plain text
