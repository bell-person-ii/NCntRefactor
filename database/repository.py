from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from database.orm import PeopleCount


class PeopleCountRepository:
    engine = create_engine('mysql+pymysql://root:1234@localhost:3306/ncnt', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    @classmethod
    def createPeopleCount(cls,head_count,time):
        print("호출2")
        peopleCount = PeopleCount(head_count=head_count,time=time)
        cls.session.add(peopleCount)
        cls.session.commit()

    @classmethod
    def findRecentOne(cls):
        peopleCount:PeopleCount = cls.session.query(PeopleCount).order_by(PeopleCount.time.desc()).first()
        return peopleCount

