from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..db_config import *

engine = create_engine(f"{DB_NAME}+{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_IP}/{DB_TABLENAME}")
engine.connect()

Session = sessionmaker(bind=engine)

Base = declarative_base()