from bottle import Bottle, run, template

app=Bottle()

@app.route('/hello')
def hello():
	return "hello world!"

run(app, host='localhost', port=8080)