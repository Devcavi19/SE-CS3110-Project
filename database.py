"""Database module for the application."""

try:
    from flask import Flask, render_template
except ImportError:
    raise ImportError("Please install Flask using: pip install -r requirements.txt")

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('base.html')

@app.route('/home')
def home():
    """Render the home page."""
    return render_template('base.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/github')
def github():
    """Render the GitHub page."""
    return render_template('github.html')

@app.route('/signin')
def signin():
    """Render the sign-in page."""
    return render_template('signin.html')

@app.route('/signup')
def signup():
    """Render the sign-up page."""
    return render_template('signup.html')

@app.route('/feedback')
def feedback():
    """Render the feedback page."""
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)