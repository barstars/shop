from fastapi import APIRouter, Depends, Request, Cookie, Response
from fastapi.responses import FileResponse

from app.models.users import UserRegister, UserDatas, UserLogin
from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/login",
	tags=["login"])

# REGISTER
@router.post("/reg")
async def register_post(uRegis: UserRegister,
					request: Request,
					response: Response,
					db: AsyncGenerator = Depends(get_db)
					):
    data = UserDatas(
        **uRegis.dict(),
        ip_address=request.client.host,
        useragent=request.headers.get("user-agent"),
    )

    auth = Auth(db)
    id_ = await auth.register(data=data)

    if id_:
        cookies_data = {"id":str(id_)}
        response.set_cookie(key="cookies_data", value=json.dumps(cookies_data))
        return {"id": id_}
    else:
        return {"data": "username уже существует"}

@router.get("/reg")
async def register_get():
    return FileResponse("frontend/register/index.html")


# LOGIN
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
        cookies_data = {"id":str(id_)}
        response.set_cookie(key="cookies_data", value=json.dumps(cookies_data))
        return id_
    else:
        return None