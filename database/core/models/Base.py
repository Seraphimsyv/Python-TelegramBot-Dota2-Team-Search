from ...core import cursor

class BaseManager:

    @classmethod
    def insertOne(cls, **kwargs) -> None:
        cursor.execute(cls.__table__.insert().values(**kwargs))

    @classmethod
    def insertMany(cls, *args) -> None:
        cursor.execute(cls.__table__.insert().valuer(*args))