from flask import Flask
app = Flask(__name__) #name of the module, if we run this file __name__="__main__"

@app.route("/")

@app.route("/home") #decorator: pass a function to the existing function "route"
def home():
    return "<h1>Tutorial 1 Home Page </h1>"

@app.route("/about")
def about():
    return "<h1>About Page </h1>"

if __name__=='__main__': #to directly run flask app from executing this file
    app.run(debug=True)# debug mode: changes appear after page is reload