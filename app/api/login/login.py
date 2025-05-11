from fastapi import APIRouter, Depends, Response
from fastapi.responses import FileResponse

from app.models.users import UserLogin
from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/login",
	tags=["login"])

@router.get("/")
async def login_get():
    return FileResponse("frontend/login/index.html")

@router.post("/")
async def login_post(ulogin: UserLogin,
                    response: Response,
                    db: AsyncGenerator = Depends(get_db)):
    auth = Auth(db)
    id_ = await auth.login(data=ulogin)

    if id_:
        cookies_data = {"id":id_}
        month = 5
        max_age = (((60*60)*24)*(30*month))
        response.set_cookie(key="cookies_data", value=json.dumps(cookies_data), max_age=max_age)
        return id_
    else:
        return None