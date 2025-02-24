from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models import db, User
from config import config
import os

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)

    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('signin'))
            return f(*args, **kwargs)
        return decorated_function

    # Route definitions
    @app.route('/')
    def index():
        return redirect(url_for('signin'))

    @app.route('/home')
    @login_required
    def home():
        fname = session.get('fname', 'User')
        return render_template('home.html', fname=fname)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/feedback', methods=['GET', 'POST'])
    def feedback():
        if request.method == 'POST':
            # Handle feedback submission
            flash('Thank you for your feedback!', 'success')
            return redirect(url_for('home'))
        return render_template('feedback.html')

    @app.route('/signin', methods=['GET', 'POST'])
    def signin():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['fname'] = user.fname
                session.permanent = True
                return redirect(url_for('home'))
            
            flash('Invalid email or password', 'error')
        return render_template('signin.html')

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        session.pop('fname', None)
        return redirect(url_for('signin'))

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            
            if User.query.filter_by(email=email).first():
                flash('Email already exists', 'error')
                return redirect(url_for('signup'))
            
            hashed_password = generate_password_hash(password)
            new_user = User(fname=fname, lname=lname, email=email, password=hashed_password)
            
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful! Please sign in.', 'success')
            return redirect(url_for('signin'))
            
        return render_template('signup.html')

    @app.route('/simulation')
    def simulation():
        return render_template('simulation.html')

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG', 'development'))
    with app.app_context():
        db.create_all()
    app.run()
