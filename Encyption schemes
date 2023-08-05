#they produce the same result the methods and structures are what's different when it comes to Enryption as long as there suffcient obfuscation that generally consider a success

first method with import
import string

Library = string.ascii_uppercase + string.digits + "_"
List = ["hello there these codes were done by mansour and ahmed"]
encrypted_list = []
for item in List:
  encrypted_list.append(Library[item % 37])
print("Encrypted list:", "".join(encrypted_list))

second method without import
LIBRARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

msg = "hello there these codes were done by mansour and ahmed".split()

encrypted_message = ""

for i in range(len(msg)):
  encrypted_message += LIBRARY[int(msg[i]) % 37]

print("picoCTF{", end='')
print(encrypted_message, end='')


third method without import but the modular has an inverse value meaning it starts from 1 and is to the power of -1
LIBRARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

msg = "hello there these codes were done by mansour and ahmed".split()

encrypted_message = ""

for i in range(len(msg)):
  encrypted_message += LIBRARY[pow(int(msg[i]), -1, 37)]

print("picoCTF{", end='')
print(encrypted_message, end='')

#if look carfully you will see that both encryption and decryption schemes have almost identical structure which is good that is indicative of a two way code able to encrypt and decrypt text
