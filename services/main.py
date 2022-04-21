
import sqlalchemy.orm as _orm
import schemas.schemas as _schemas
import models.models as _models
import database.database as _database

#Database
def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Farms

async def create_temp(db: _orm.Session, temp: _schemas.TempCreate):
    db_temp = _models.Temp(valor = temp.valor)
    db.add(db_temp)
    db.commit()
    db.refresh(db_temp)
    return db_temp    





    





    