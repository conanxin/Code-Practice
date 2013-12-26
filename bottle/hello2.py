from bottle import Bottle, run, template

app=Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

run(app, host='localhost', port=8080)

#test: http://localhost:8080/hello/xin