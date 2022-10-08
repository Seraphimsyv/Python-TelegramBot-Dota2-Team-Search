from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy import select, and_, update
from datetime import datetime

from ..core import cursor, metadata
from ..core.models import BaseManager
from ..utils import getCurrentTimestamp, Regions

from .Users import UsersManager
from .Teammates import TeammatesManager

import random


class TargetsManager(BaseManager):

    class Target:

        def __init__(self, args) -> None:
            self.id = args[0]
            self.user_id = args[1]
            self.user = UsersManager.getUserById(args[1])
            self.rate = args[2]
            self.position = args[3]
            self.region = args[4]

    __table__ = Table(
        'targets', metadata,
        Column('id', Integer, nullable=False, unique=True, primary_key=True, autoincrement=True),
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('rate', Integer, nullable=False),
        Column('position', Integer, nullable=False),
        Column('region', String, nullable=False, default=Regions.RU),
    )

    @classmethod
    def getUserTargets(cls, user_id):
        query = select([cls.__table__], cls.__table__.c.user_id == user_id)
        return cursor.execute(query).fetchone()
 
    @classmethod
    def setUserTargetIfNotExist(cls, data) -> None:
        query = select([cls.__table__], cls.__table__.c.user_id == data['user_id'])
        if len(cursor.execute(query).fetchall()) == 0:
            cls.insertOne(**data)
        else:
            query = (update(cls.__table__).where(
                cls.__table__.c.user_id == data['user_id']).values(
                        user_id=data['user_id'],
                        rate=data['rate'],
                        position=data['position'],
                        region=data['region']
                    )
            )
            cursor.execute(query)


    @classmethod
    def getUserFromTarget(cls, user_id):
        query = select([cls.__table__], cls.__table__.c.user_id == user_id)
        target = cursor.execute(query).fetchone()

        """ Check if exists user with target search parameters """
        if target == None:
            return {"type": "error", "msg": "Target parameters of user not exists"}

        """ Search users with target parameters """
        user = UsersManager.getUserById(user_id)

        query = select(
            [UsersManager.__table__],
            and_(
                UsersManager.__table__.c.id > user.last_selected_id+1,
                UsersManager.__table__.c.tg_id != user_id,
                UsersManager.__table__.c.status == True,
                UsersManager.__table__.c.rate <= target.rate+500,
                UsersManager.__table__.c.rate >= target.rate-500,
                UsersManager.__table__.c.position == target.position,
                UsersManager.__table__.c.region == target.region
            )
        )

        result = cursor.execute(query).fetchone()

        if result != None:
            UsersManager.updateUserLastSelective(user.tg_id, result[0]+1)

            now = datetime.fromtimestamp(getCurrentTimestamp())
            old = datetime.fromtimestamp(result[5])

            if (now-old).days > 7:
                UsersManager.setUserNotActive(result[1])

                return cls.getUserFromTarget(user_id)
            
            if TeammatesManager.checkTeammates(user_id, result[1]) == False:
                
                return result

            else:

                UsersManager.setUserNotActive(result[1])

                return cls.getRandomUser(user_id)
            
        else:
            """ Check if users exists with target parameters """
            query = select(
                [UsersManager.__table__],
                and_(
                    UsersManager.__table__.c.id > user.last_selected_id,
                    UsersManager.__table__.c.tg_id != user_id,
                    UsersManager.__table__.c.status == True,
                    UsersManager.__table__.c.rate <= target.rate+500,
                    UsersManager.__table__.c.rate >= target.rate-500,
                    UsersManager.__table__.c.position == target.position,
                    UsersManager.__table__.c.region == target.region
                )
            )
            result = cursor.execute(query).fetchall()
            if len(result) > 0 and result[-1][0] < user.last_selected_id:
                UsersManager.updateUserLastSelective(user.tg_id, 0)
                return cls.getUserFromTarget(user_id)

            """ Return error if users not exists with search parameters """
            return {"type": "error", "msg": "Not exists users for target"}


    @classmethod
    def getRandomUser(cls, user_id):
        #query = select([UsersManager.__table__], and_(UsersManager.__table__.c.status == True, UsersManager.__table__.c.tg_id != user_id))
        query = select([UsersManager.__table__], UsersManager.__table__.c.status == True)
        result = cursor.execute(query).fetchall()

        if len(result) > 1:

            inx = random.randint(0, len(result)-1)

            now = datetime.fromtimestamp(getCurrentTimestamp())
            old = datetime.fromtimestamp(result[inx][5])
            
            if (now-old).days > 7:
                UsersManager.setUserNotActive(result[inx][1])

                return cls.getRandomUser(user_id)

            if TeammatesManager.checkTeammates(user_id, result[0][1]) == False:
                
                return result[inx]

            else:

                UsersManager.setUserNotActive(result[inx][1])

                return cls.getRandomUser(user_id)

        elif len(result) == 1:

            now = datetime.fromtimestamp(getCurrentTimestamp())
            old = datetime.fromtimestamp(result[0][5])
            
            if (now-old).days > 7:
                UsersManager.setUserNotActive(result[0][1])

                return cls.getRandomUser(user_id)

            if TeammatesManager.checkTeammates(user_id, result[0][1]) == False:
                return result[0]
            else:
                return {"type": "error", "msg": "Active users not available"}

        return {"type": "error", "msg": "Active users not available"}
