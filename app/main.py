from fastapi import FastAPI
from app.database import Base, engine

from app.routers import users, companies, experiences

app = FastAPI(title="Placement Tracker API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(companies.router)
app.include_router(experiences.router)


@app.get("/")
def root():
    return {"message": "Placement Tracker API running"}
@app.get("/favicon.ico")
async def favicon():
    return {}