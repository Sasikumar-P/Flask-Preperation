
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
@app.route('/')
def index():
	if 'username' in session:
		username=session['username']
		return 'Logged in as ' + username + '<br>' + "<b><a href='/logout'>click here to log out</a></b>"
	return "You are not logged in <br><a href='/login'></b>" + "click here olog in</b></a>"
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return ''
@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))
if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=12345, use_reloader=True)

