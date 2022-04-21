from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import base64

#services
import services.main as _mainServices
#schemas
import schemas.schemas as _schemas

app = _fastapi.FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Api redes",
    description="Api redes",
    version="2.0",
    openapi_url="/openapi.json",   
)

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_mainServices.create_database()

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')


#####################################################################################################
#Temp

@app.post("/temps/", response_model=_schemas.Temp, tags=["temperaturas"])
async def create_temp(temp: _schemas.TempCreate, db: _orm.Session = _fastapi.Depends(_mainServices.get_db)):
    return await _mainServices.create_temp(db=db, temp=temp)


