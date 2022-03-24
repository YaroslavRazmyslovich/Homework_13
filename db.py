from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


url = 'sqlite:///local.db'

engine = create_engine(url, echo=False)
Base = declarative_base()

 
def execute(*args, **kwargs):
    with engine.connect() as conn:
        return conn.execute(*args, **kwargs)

