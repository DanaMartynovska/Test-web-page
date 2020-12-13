from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/') #main
def index():
    return render_template('index.html')


@app.route('/comments') #comments
def com():
    return render_template('comments.html')

@app.route('/user/<string:name>/<int:id>') #user
def user(name, id):
    return 'User page: ' + name + '-' + str(id)


app.run(debug=True)