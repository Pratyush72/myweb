import sqlalchemy
import sqlalchemy.ext.declarative as abc
import pymysql

class Connect:
    engine = sqlalchemy.create_engine(
        'mysql+pymysql://root:toor@127.0.0.1:3306/study?charset=utf8mb4'
    )
    Base = abc.declarative_base()

def createTable():
    Connect.Base.metadata.create_all(Connect.engine)

def connectToDatabase():
    Session1 = sqlalchemy.orm.sessionmaker(bind=Connect.engine)
    return Session1
