from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change to a secure key

# Database configuration (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/users' (You can change the database directory)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database Model for Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

# Routes
@app.route('/')
def index():
    return redirect(url_for('signin'))  # Redirect to sign-in page
    return redirect(url_for('signin'))  # Redirect to sign-in page

@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the user from the database
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Signed in successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to the base.html page
        else:
            message = 'Invalid email or password!'

    return render_template('signin.html', message=message)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists! Please sign in.', 'warning')
            return redirect(url_for('signin'))

        # Hash the password and save the user to the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(fname=fname, lname=lname, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Successfully signed up! Please sign in.', 'success')
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/simulation')
def simulation():
    return render_template('simulation.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
