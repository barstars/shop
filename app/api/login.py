from fastapi import APIRouter, Depends, Request, Cookie, Response
from fastapi.responses import FileResponse

from app.models.users import UserLogin, UserDatas
from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/login",
	tags=["login"])

@router.post("/reg")
async def register_post(uLogin: UserLogin,
					request: Request,
					response: Response,
					db: AsyncGenerator = Depends(get_db)
					):

    ip_address = request.client.host
    useragent = request.headers.get("user-agent")

    data = UserDatas(
        **uLogin.dict(),
        ip_address=ip_address,
        useragent=useragent,
    )

    auth = Auth(db)
    id_ = await auth.register(data=data)
    cookies_data = {"id":str(id_)}
    if id_:
    	response.set_cookie(key="cookies_data", value=json.dumps(cookies_data))
    	return {"id": id_}
    else:
    	return {"data": "username уже существует"}

@router.get("/reg")
async def register_get():
    return FileResponse("frontend/register/index.html")