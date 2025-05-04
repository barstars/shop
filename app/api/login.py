from fastapi import APIRouter, Depends, Request, Cookie, Response

from app.models.users import UserLogin, UserDatas
from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/login",
	tags=["login"])

@router.get("/")
async def login_html():
	return {"test": "OK"}

@router.post("/reg")
async def register(uLogin: UserLogin,
					request: Request,
					response: Response,
					db: AsyncGenerator = Depends(get_db)
					):#cookies_data: str = Cookie(default="{}")
	# cookies = json.loads(cookies_data)

    ip_address = request.client.host
    useragent = request.headers.get("user-agent")

    # setting = cookies.get("setting")

    data = UserDatas(
        **uLogin.dict(),
        ip_address=ip_address,
        useragent=useragent,
    )

    auth = Auth(db)
    id_ = await auth.register(data=data)
    if id_:
    	response.set_cookie(key="cookies_data", value=id_)
    	return {"id": id_}
    else:
    	return {"data": "username уже существует"}