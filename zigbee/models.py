from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import DB

Base = declarative_base()


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer)
    dtype = Column(String(1), nullable=False)
    path = Column(String(120), nullable=False)
    message = Column(String(128), nullable=True)
    timestamp = Column(Integer)


engine = create_engine(DB)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
