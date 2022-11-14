from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, select
meta = MetaData()

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

users = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True, autoincrement=True), 
   Column('first_name', String), 
   Column('last_name', String), 
   Column('email', String, unique=True), 
   Column('password', String), 
)

async def init_models():
    async with db.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

@app.route('/db/')
def testdb():
    stmt = select(users)
    str=""
    with db.connect() as conn:
        for row in conn.execute(stmt):
            str=str+" "+row

    return str
