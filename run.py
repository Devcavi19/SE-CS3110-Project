from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    "user@example.com": "password123"  # You can replace this with real user data from your database
}

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/github')
def github():
    return render_template('github.html')

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Simple authentication check (replace with actual logic)
        if users.get(email) == password:
            # Redirect to the base.html (or home page after successful login)
            return redirect(url_for('home'))  # Replace 'home' with your base route
        else:
            message = "Invalid credentials. Please try again."
            return render_template('signin.html', message=message)
    
    return render_template('signin.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get form data
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            message = "Passwords do not match"
            return render_template('signup.html', message=message)

        # Check if the email is already taken (replace with actual database check)
        if email in users:
            message = "Email is already taken"
            return render_template('signup.html', message=message)
        
        # Register the user (add them to your database here)
        users[email] = password

        # Redirect to the sign-in page after successful registration
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)