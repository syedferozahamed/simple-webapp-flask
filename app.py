#first change
import os
from flask import Flask
app = Flask(__name_sample__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'
# use port 8080 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
