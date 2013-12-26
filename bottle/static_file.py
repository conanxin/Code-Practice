from bottle import Bottle, run, template, static_file

app=Bottle()

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@app.route('/images/<filename:re:.*\.png>#')
def send_image(filename):
	return static_file(filename, root='/path/to/images/files', mimetype='image/png') 

@app.route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='/path/to/static/files')

run(app, host='localhost', port=8080)

