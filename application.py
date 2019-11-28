from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


# az webapp up --sku FREE -n "inviteapp2" -l "Central US"
