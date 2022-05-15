from flask import *
from hashlib import sha256

app = Flask(__name__)

@app.route("/index", methods = ["get"])

def pycoin():
      email = open("emails.txt", "a")
      email.close()
      
      login = request.args.get("login")
      signup = request.args.get("signup")
      block = request.args.get("block")

      if signup != "" and login == "":
            result = sha256(signup.encode("ascii")).hexdigest()
            my_boolean = False

            with open("emails.txt", "r") as file:
                  for line in file:
                        if str(result + "\n") == str(line):
                              my_boolean = True
                              break

            if my_boolean == True:
                  return "user already registered"

            if  my_boolean == False:
                  email = open("emails.txt", "a")
                  email.write(result + "\n")
                  email.close()
                  return "registered successfully"

      if login != "":
            my_boolean = False
            result = sha256(login.encode("ascii")).hexdigest()

            with open("emails.txt", "r") as file:
                  for line in file:
                        if str(result + "\n") == str(line):
                              print(str(result + "\n"))
                              print(str(line))
                              my_boolean = True
                              break

            if my_boolean == True:
                  result = sha256(block.encode("ascii")).hexdigest()

                  if "000000" in result:
                        return "hash found"

                  else:
                        return "not a valid hash"

            if my_boolean == False:
                  return "user not found"

      else:
            return "ERROR 404"
                        
app.run()
