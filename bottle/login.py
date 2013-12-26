from bottle import Bottle, run, template, request, get, post

app=Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@app.get('/login')
def login_form():
	return	'''<form method="POST" action="/login">
				<input name="name"	type="text"	/>
				<input name="password"	type="password"	/>
				<input type="submit"	/>
			   </form>'''

@app.post("/login")
def login_submit():
	name	=	request.forms.get('name')
	password=	request.forms.get('password')
	if check_login(name, password):
		return	"<p>Your login was correct</p>"
	else:
		return	"<p>Login failed</p>"

run(app, host='localhost', port=8080)

