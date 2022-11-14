from flask import Flask, render_template
from sqlalchemy import insert, create_engine, Table, Column, Integer, String, MetaData, select
meta = MetaData()

app = Flask(__name__)

# change to name of your database; add path if necessary
DB_NAME = 'bank.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db=create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

@app.route('/')
def hello():
    return render_template('index.html')

users = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True, autoincrement=True), 
   Column('first_name', String), 
   Column('last_name', String), 
   Column('email', String, unique=True), 
   Column('password', String), 
)


meta.create_all(db)

@app.route('/db/')
def testdb():
    stmt = select(users)
    with db.connect() as conn:
        return render_template('db.html', result=conn.execute(stmt))
