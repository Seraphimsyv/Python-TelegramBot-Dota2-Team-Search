from sqlalchemy import ForeignKey, Table, Column, Integer, String, Float
from sqlalchemy import select

from ..core import cursor, metadata
from ..core.models import BaseManager
from ..utils import getCurrentTimestamp

from .Users import UsersManager


class ReportsManager(BaseManager):

    class Report:

        def __init__(self, args) -> None:
            self.id = args[0]
            self.user_reporter = UsersManager.getUserById(args[1])
            self.user_reported = UsersManager.getUserById(args[2])
            self.reason = args[3]
            self.timestamp = args[4]

    __table__ = Table(
        'reports', metadata,
        Column('id', Integer, nullable=False, unique=True, primary_key=True, autoincrement=True),
        Column('user_reporter_id', Integer, ForeignKey('users.id')),
        Column('user_reported_id', Integer, ForeignKey('users.id')),
        Column('reason', String),
        Column('timestamp', Float, default=getCurrentTimestamp)
    )