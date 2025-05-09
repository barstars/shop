from fastapi import FastAPI
from app.api import login, home, get_static_files

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
app.include_router(home.router)
app.include_router(get_static_files.router)
