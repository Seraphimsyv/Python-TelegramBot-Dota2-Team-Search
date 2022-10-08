import datetime


def getCurrentTimestamp() -> float:
    ct = datetime.datetime.now()
    return ct.timestamp()


class Regions:
    RU = "RU"