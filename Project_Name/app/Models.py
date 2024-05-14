from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.dialects.postgresql import JSON
Base = declarative_base()


class services(Base):
    __tablename__ = "table_name"
    id = Column(Integer, primary_key=True)

passsword = 'not_password'
ip_and_port = 'ip:port'

engine = create_engine(f'postgresql://postgres:{password}@{ip_and_port}')
Base.metadata.create_all(engine)
