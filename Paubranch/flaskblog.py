from flask import Flask, render_template #we import the class Flask, we import the function to render our HTML templates
app = Flask(__name__)


posts = [
	{	
		'author': 'Pau Pulido',
		'title': 'Blog post 1',
		'content': 'Flask Mola, nen',
		'date_posted': 'April 23, 2020'
	},
	{
		'author': 'Pedro Sanchez',
		'title': 'Blog post 2',
		'content': 'Confínate mamón',
		'date_posted': 'April 24, 2020'
	}

]
@app.route('/') #decorator
@app.route('/home') #a return home route for our app
def home():
    return render_template('home.html', posts=posts)


if __name__ == "__main__": #to run debug in debug mode in case we want ro run this script directly on python, by typing python flaskblog.py on the terminal.
	app.run(debug=True)

@app.route('/about') #we add another app route called about, which is going to be a new page
def about():
    return render_template('about.html', title='About')
