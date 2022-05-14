from flask import *
from hashlib import sha256

app = Flask(__name__)

@app.route("/index", methods = ["get"])

def pycoin():
      email = request.args.get("email")
      block = request.args.get("block")

      if email == "49dab445ccba34f55aa2aa7b31f93edb5d9db7faff1834735013d24f57f2f988":
            result = sha256(block.encode("ascii")).hexdigest()

            if "00000000" in result:
                  return "hash found"

            else:
                  return "not a valid hash"

      else:
            return "user not found"

      

app.run()
