from sqlalchemy import insert, select
from db import Base, engine, execute
from models import User, Address

Base.metadata.create_all(engine)


def insert_many():
    query = insert(User)
    execute(query,[{
        'name': 'Leva',
        'fullname': 'Lev Leschenko',
        'gender': 'male',
        'age': 65},{
        'name': 'Luke',
        'fullname': 'Luke Skywalker',
        'gender': 'male',
        'age': 38},{
        'name': 'Luc',
        'fullname': 'Luc Besson',
        'gender': 'male',
        'age': 63},{
        'name': 'Dita',
        'fullname': 'Dita von Teese',
        'gender': 'female',
        'age': 43},{
        'name': 'Don',
        'fullname': 'Vito Corleone',
        'gender': 'male',
        'age': 68},])
#insert_many ()

def select_users():
    query = (
        select (User.name)
            .where(
                User.name.like('L%') |
                User.name.like('D%') 
            )
            .where(
                User.gender == 'male'
            )
            .limit (3)
            .order_by(User.age.desc())
    )
    with engine.connect() as conn:
        user = conn.execute(query)
        users = list (user)
    for user in users:
        print (dict(user))
select_users()
        
