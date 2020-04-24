from flask import Flask, render_template
app = Flask(__name__) #name of the module, if we run this file __name__="__main__"

dataBase=[
    {
        "author":"Corey Schafer",
        "title":"Blog post 1",
        "content":"First post content",
        "data_posted": "April 20,2018"
    },
    {
        "author":"Jane Doe",
        "title":"Blog Post2",
        "content":"Second post content",
        "date_posted": "April 21, 2018"
    }
]


@app.route("/")

@app.route("/home") #decorator: pass a function to the existing function "route"
def home():
    return render_template("home2.html",posts=dataBase)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__=='__main__': #to directly run flask app from executing this file
    app.run(debug=True)# debug mode: changes appear after page is reload