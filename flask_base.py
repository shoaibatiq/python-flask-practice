from flask import Flask

app = Flask(__name__)
@app.route('/')
def Homepage():
	return "<h1>This is the homepage\nTo see puppy latin name route to /puppy_latin/<name></h1>"

@app.route('/info/')
def info():
	return "<h1>This is a static information page.</h1>"

@app.route('/puppy_latin/<name>/')
def dynamic_user_page(name):
	latin_name=name+'y' if name[-1]!='y' else name[:-1]+'iful'
	return f"<h1>Hi {name}! Your puppy latin name is: {latin_name}.</h1>"
		
if __name__ == '__main__':
	app.run(debug=True)