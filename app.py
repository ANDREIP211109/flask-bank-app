from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'bank.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

db.init_app(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/db/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as error:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(error) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
