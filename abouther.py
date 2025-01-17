from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loggedin')
def login():
    return render_template('loggedin.html')

if __name__ == '__main__':
   app.run()