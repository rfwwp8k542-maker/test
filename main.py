from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registrer', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
            username = request.form['username']
    return render_template('registrer.html')
@app.route('/login', methods={'GET', 'POST'})
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))