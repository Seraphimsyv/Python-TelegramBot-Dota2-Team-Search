from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy import select, and_

from ..core import cursor, metadata
from ..core.models import BaseManager

from .Users import UsersManager


class TeammatesManager(BaseManager):

    class Teammate:

        def __init__(self, args) -> None:
            self.id = args[0]
            self.user = UsersManager.getUserById(args[1])
            self.teammmate = UsersManager.getUserById(args[2])

    __table__ = Table(
        'teammates', metadata,
        Column('id', Integer, nullable=False, unique=True, primary_key=True, autoincrement=True),
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('teammate_id', Integer, ForeignKey('users.id')),
    )

    @classmethod
    def createPairIfNotExists(cls, user_id, teammate_id):
        query_1 = select([cls.__table__], and_(cls.__table__.c.user_id == user_id, cls.__table__.c.teammate_id == teammate_id))
        query_2 = select([cls.__table__], and_(cls.__table__.c.user_id == teammate_id, cls.__table__.c.teammate_id == user_id))
        if cursor.execute(query_1).fetchone() == None and cursor.execute(query_2).fetchone() == None:
            cls.insertOne(user_id=user_id, teammate_id=teammate_id)
            cls.insertOne(user_id=teammate_id, teammate_id=user_id)

    @classmethod
    def checkTeammates(cls, user_id, teammate_id):
        query_1 = select([cls.__table__], and_(cls.__table__.c.user_id == user_id, cls.__table__.c.teammate_id == teammate_id))
        query_2 = select([cls.__table__], and_(cls.__table__.c.user_id == teammate_id, cls.__table__.c.teammate_id == user_id))
        if cursor.execute(query_1).fetchone() == None and cursor.execute(query_2).fetchone() == None:
            return False
        return True

    @classmethod
    def getAllTeammatesOfUser(cls, user_id):
        query = select([cls.__table__], cls.__table__.c.user_id == user_id)
        return cursor.execute(query).fetchall()