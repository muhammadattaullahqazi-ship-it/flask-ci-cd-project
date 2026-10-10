from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)

# Secret key must come from an environment variable - no weak fallback.
# The app will refuse to start if FLASK_SECRET isn't set.
app.secret_key = os.environ["FLASK_SECRET"]

# Simple check to demonstrate environment variables/configuration
VERSION = os.environ.get("APP_VERSION", "1.0.0")


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        # placeholder validation: accept non-empty credentials
        if username and password:
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Please provide username and password', 'danger')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=user, version=VERSION)


if __name__ == '__main__':
    # Debug mode is OFF by default. Flask's debug mode exposes the Werkzeug
    # interactive debugger, which allows remote code execution if the app
    # is reachable from the internet. Only enable it locally via:
    #   FLASK_DEBUG=1 python app.py
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)