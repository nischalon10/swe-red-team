from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/logged_in')
def main():
    return render_template('app.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Add your logic to check username and password here
    return redirect(url_for('main'))

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    # Add your logic to create a new user here
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)