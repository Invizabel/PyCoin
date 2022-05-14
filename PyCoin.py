from hashlib import sha256
import os

os.system("clear")

def pycoin(email):
    block = 0
    email = sha256(email.encode("ascii")).hexdigest()
    print("hashed email: " + str(email))
    email = str(email)
    blocks_mined = 0

    while True:
        block += 1
        result = sha256(str(block).encode("ascii")).hexdigest()

        if "0000000000000000" in result:
            blocks_mined += 1
            print("blocks mined: " + blocks_mined)

email = input("Enter email: ")
os.system("clear")
pycoin(email)
