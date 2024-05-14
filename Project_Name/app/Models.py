from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.dialects.postgresql import JSON
Base = declarative_base()


class services(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)


engine = create_engine('postgresql://postgres:Igus3r1234@10.8.1.11:5432')
Base.metadata.create_all(engine)
