import datetime as _dt
from sqlalchemy import Column, Float, String, Integer, DateTime, Boolean, ForeignKey
import sqlalchemy.orm as _orm
import database.database as _database


class Temp(_database.Base):
    __tablename__ ="temperatura_medicoes"
    medicao_id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Integer)


