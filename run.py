from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)