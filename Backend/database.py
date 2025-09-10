from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base




# crete the database 
DB_URL = "mysql+pymysql://root:nilum%402002@localhost:3306/KandyPack_DB"
engine = create_engine(DB_URL)
Session_local = sessionmaker(bind = engine, autoflush= False,autocommit = False)
Base = declarative_base()
