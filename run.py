from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user data (replace with real authentication)
users = {
    'user1': 'password1',
    'user2': 'password2'
}
#Ja a pan Spanek nejsme velky kamaradi
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index', methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
   app.run(debug=True)
   
    
else:
    gunicorn_app = app
