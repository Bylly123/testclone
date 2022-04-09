import random
import string

length = 16

password = "".join(random.sample(string.ascii_lowercase, k=length))

print("\nHere is your password: ",password)

input("\nenter to leave")