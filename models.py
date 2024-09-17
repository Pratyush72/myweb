# from datetime import datetime
# from sqlalchemy import Column, Integer, String, DateTime
# from const import Connect

# class User(Connect.Base):
#     __tablename__ = 'user_phone'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(50), nullable=False  )
#     email = Column(String(120), nullable=False, unique=True)
#     password = Column(String(200), nullable=False)
#     created_time = Column(DateTime, default=datetime.now)

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime,Boolean
from const import Connect

class User(Connect.Base):
    __tablename__ = 'user_phone'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    is_subscribed = Column(Boolean, default=False)
    subscription_start_date = Column(DateTime, nullable=True)
    subscription_end_date = Column(DateTime, nullable=True)   
    created_time = Column(DateTime, default=datetime.now)
