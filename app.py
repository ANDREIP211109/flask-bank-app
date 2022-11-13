from flask import Flask, render_template

app = Flask(__name__)


data={
    'title': 'Bank'
}

@app.route('/')
def hello():
    return render_template('index.html', data=data)