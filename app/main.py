from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api import home, admin
from app.api.login import login, register

from app.db.crud.start import action_all_table

from contextlib import asynccontextmanager

app = FastAPI()

@app.on_event("startup")
async def startup_event():
	await action_all_table()
	print("STRATUP")

@app.on_event("shutdown")
async def shutdown_event():
	print("OUT")

app.include_router(login.router)
app.include_router(register.router)

app.include_router(admin.router)

app.include_router(home.router)
app.mount("/static", StaticFiles(directory="frontend"), name="static")
