from flask import Flask, render_template, request, redirect, url_for, session
from app import System
from app import Income, Expense


app = Flask(__name__)
app.secret_key = 'some_secret_key'  # Secret key for sessions

system = System()


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = system.login(username, password)
#         if user:
#             session['username'] = user.username
#             return redirect(url_for('dashboard'))
#     return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = system.register(username, password)
        if user:
            session['username'] = user.username
            return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    user = system.get_user(session.get('username'))
    if not user:
        return redirect(url_for('index'))
    summary = user.summary()
    transactions = user.view_transactions()
    return render_template('dashboard.html', username=session['username'], balance=summary['Balance'])

# Additional routes for adding transactions, viewing by category, etc.


@app.route('/demo')
def demo():
    # Mock data for demonstration
    username = "DemoUser"
    summary = {
        'Total Income': 6000,
        'Total Expense': 1000,
        'Balance': 5000
    }
    transactions = [Income(5000, "Salary", "Work"),
                    Expense(50, "Lunch", "Food")]

    return render_template('dashboard.html', username=username, summary=summary, transactions=transactions)


@app.route('/about')
def about():
    return render_template('documentation.html')


if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from app import System, User, Income, Expense


# app = Flask(__name__)
# # secret key for session
# app.secret_key = 'your_secret_key_here'
# system = System()


# @app.route('/')
# def index():
#     return "Welcome to the Personal Finance Tracker!"


# @app.route('/dashboard/<username>')
# def dashboard(username):

#     user = system.login(username, "securepassword")
#     if user:
#         return render_template('dashboard.html', username=username, balance=user.get_balance())
#     return "User not found", 404


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = system.register(username, password)
#         if user:
#             session['username'] = username  # This keeps the user logged in
#             return redirect(url_for('dashboard', username=username))
#         else:
#             flash("Username already exists!")
#     return render_template('register.html')


# if __name__ == "__main__":
#     app.run(debug=True)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = system.login(username, password)
#         if user:
#             session['username'] = username  # This keeps the user logged in
#             return redirect(url_for('dashboard', username=username))
#         else:
#             flash("Invalid credentials!")
#     return render_template('login.html')
