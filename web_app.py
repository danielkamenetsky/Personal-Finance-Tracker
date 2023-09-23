from flask import Flask, render_template, request, redirect, url_for, session, flash
from app import System, User, Income, Expense


app = Flask(__name__)
# secret key for session
app.secret_key = 'your_secret_key_here'
system = System()


@app.route('/')
def index():
    return "Welcome to the Personal Finance Tracker!"


@app.route('/dashboard/<username>')
def dashboard(username):

    user = system.login(username, "securepassword")
    if user:
        return render_template('dashboard.html', username=username, balance=user.get_balance())
    return "User not found", 404


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = system.register(username, password)
        if user:
            session['username'] = username  # This keeps the user logged in
            return redirect(url_for('dashboard', username=username))
        else:
            flash("Username already exists!")
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = system.login(username, password)
        if user:
            session['username'] = username  # This keeps the user logged in
            return redirect(url_for('dashboard', username=username))
        else:
            flash("Invalid credentials!")
    return render_template('login.html')
