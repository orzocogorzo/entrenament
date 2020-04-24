from flask import Flask


app = Flask(__name__)


posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
    }
]
@app.route("/")
@app.route("/home")
def home ():
    return "<h1>Home Page</h1>"
    
    
@app.route("/about")
def about ():
    return "<h1>About Page</h1>"
    
    
if __name__ == "__main__":
    app.run(debug=True)
