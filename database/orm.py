from sqlalchemy import DateTime, Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PeopleCount (Base):
    __tablename__ = "people_count"

    id = Column(Integer,primary_key= True, index=True)
    head_count = Column(Integer,nullable=False)
    time = Column(DateTime,nullable=False)


    def __init__(self,head_count,time):
        self.head_count=head_count
        self.time=time
