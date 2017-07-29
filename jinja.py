
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hello/<user>')
def hello_name(user):
	return render_template('hai.html', name=user)
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)
