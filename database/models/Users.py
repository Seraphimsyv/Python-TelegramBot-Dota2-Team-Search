from sqlalchemy import Table, Column, Integer, String, Boolean, Float
from sqlalchemy import select, update

from ..core import cursor, metadata
from ..core.models import BaseManager
from ..utils import getCurrentTimestamp, Regions


class UsersManager(BaseManager):

    class User:

        def __init__(self, args):
            self.id = args[0]
            self.tg_id = args[1]
            self.first_name = args[2]
            self.username = args[3]
            self.language_code = args[4]
            self.registration_timestamp = args[5]
            self.name = args[6]
            self.status = args[7]
            self.rate = args[8]
            self.position = args[9]
            self.region = args[10]
            self.description = args[11]
            self.last_active = args[12]
            self.last_selected_id = args[13]
            self.__data = args
        
        def to_array(self):
            return self.__data

    __table__ = Table(
        'users', metadata,
        # Telegram settings
        Column('id', Integer, nullable=False, unique=True, primary_key=True, autoincrement=True),
        Column('tg_id', Integer, nullable=False),
        Column('first_name', String, nullable=False),
        Column('username', String, nullable=True),
        Column('language_code', String, nullable=False),
        Column('registration_timestamp', Float, nullable=False, default=getCurrentTimestamp),
        # Dota settings
        Column('name', String, nullable=False),
        Column('status', Boolean, default=True),
        Column('rate', Integer, nullable=False),
        Column('position', Integer, nullable=False),
        Column('region', String, nullable=False, default=Regions.RU),
        Column('description', String, nullable=False),
        Column('last_active', Float, nullable=False, default=getCurrentTimestamp),
        Column('last_selected_id', Integer, nullable=True, default=0)
    )
    
    @classmethod
    def CreateOrUpdate(cls, **data):
        query = select([cls.__table__], cls.__table__.c.tg_id == data['tg_id'])
        if cursor.execute(query).fetchone() == None:
            cls.insertOne(**data)
        else:
            query = (update(cls.__table__).where(cls.__table__.c.tg_id == data['tg_id']).values(**data))
            cursor.execute(query)

    @classmethod
    def getUserById(cls, id):
        query = select([cls.__table__], cls.__table__.c.tg_id == id)
        if cursor.execute(query).fetchone() != None:
            return cls.User(cursor.execute(query).fetchone())
        return False


    @classmethod
    def setUserNotActive(cls, tg_id) -> None:
        query = (update(cls.__table__).where(cls.__table__.c.tg_id == tg_id).values(status=False))
        cursor.execute(query)

    @classmethod
    def setUserActive(cls, tg_id) -> None:
        last_active = getCurrentTimestamp()
        query = (update(cls.__table__).where(cls.__table__.c.tg_id == tg_id).values(status=True, last_active=last_active))
        cursor.execute(query)

    @classmethod
    def updateUserLastSelective(cls, tg_id, new_id) -> None:
        query = (update(cls.__table__).where(cls.__table__.c.tg_id == tg_id).values(last_selected_id=new_id))
        cursor.execute(query)

    @classmethod
    def setUserIfNotExist(cls, **kwargs) -> None:
        query = select([cls.__table__], cls.__table__.c.tg_id == kwargs['id'])
        if len(cursor.execute(query).fetchall()) == 0:
            cls.insertOne(**kwargs)