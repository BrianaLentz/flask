from flask import Flask

app = Flask(__name__) #name will be replaced by server.py

@app.route('/') # This is what we put in browser http://localhost:5000/ <--this is the base route!!!
def hello_world(): # This gets run
    # print("a request came in on '/' !!!") # This will print to terminal not webpage
    return "Hello World" # This gets returned

@app.route("/dojo")
def dojo():
    return 'Dojo!'

@app.route("/say/<string:name>")
def say_hi_(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:times>/<string:name>")
def repeat(times,name):
    return (name) * (times)


if __name__ == "__main__": # This NEEDS to be at the bottom, last thing
    app.run(debug=True)
