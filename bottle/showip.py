from bottle import Bottle, run, template, static_file

app=Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@app.route('my_ip')
def show_ip():
	ip=request.environ.get('REMOTE_ADDR')
	return "Your IP is: %s" %ip

run(app, host='localhost', port=8080)

