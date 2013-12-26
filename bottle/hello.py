from bottle import route, run

@route('/hello')
def hello():
	return "hello world!"

run(host='localhost', port=8080, debug=True)