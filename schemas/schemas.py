from typing import List
import datetime as _dt
import pydantic as _pydantic

#Temp
class TempCreate(_pydantic.BaseModel):
    valor: int

class Temp(TempCreate):
    medicao_id: int
    class Config:
	    orm_mode=True

