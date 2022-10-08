from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///sqlite3.db?check_same_thread=False') 
cursor = engine.connect()
metadata = MetaData(bind=engine)
