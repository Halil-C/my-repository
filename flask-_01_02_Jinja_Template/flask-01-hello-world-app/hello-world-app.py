from flask import Flask 
app = Flask(__name__)



@app.route("/")
def home():
    return "Hello!"

@app.route("/bye")
def theend():
    return "<h1>Good Bye. Comme Again</h1>"


if __name__ == '__main__':

    app.run(port=8080)
    # app.run(host= '0.0.0.0', port=8081)