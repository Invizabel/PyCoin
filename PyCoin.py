from hashlib import sha256
import os
import requests

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

        if "00000000" in result:
            blocks_mined += 1
            parameters = {"email": str(email), "block": str(block)}
            my_request = requests.get("http://localhost:5000/index", params = parameters)
            print(my_request.text)

email = input("Enter email: ")
os.system("clear")
pycoin(email)
