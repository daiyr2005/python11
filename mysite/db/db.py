from sqlalchemy.orm import sessionmaker, Session
from  sqlalchemy.engine import create_engine
from  sqlalchemy.ext.declarative import declarative_base


db_url = 'postgresql://postgres:admin@localhost/user_app'
engine = create_engine(db_url)


SessionLocal = sessionmaker(bind=engine)



Base = declarative_base()

