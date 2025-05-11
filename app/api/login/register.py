from fastapi import APIRouter, Depends, Request, Response, Cookie
from fastapi.responses import FileResponse

from app.models.users import UserRegister, UserDatas, UserAdminRegister
from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/register",
	tags=["register"])

# USER REGISTER
@router.post("/")
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
		cookies_data = {"id":id_}
		month = 5
		max_age = (((60*60)*24)*(30*month))
		response.set_cookie(key="cookies_data", value=json.dumps(cookies_data), max_age=max_age)
		return {"id": id_}
	else:
		return {"data": "username уже существует"}

@router.get("/")
async def register_get():
	return FileResponse("frontend/register/index.html")

###############

# ADMIN USER REGISTER

@router.post("/admin")
async def register_post(uARegis: UserAdminRegister,
					request: Request,
					response: Response,
					cookies_data: str = Cookie(default="{}"),
					db: AsyncGenerator = Depends(get_db)
					):
	cookies = json.loads(cookies_data)
	if cookies:
		id_ = cookies.get("id")
		auth = Auth(db)
		if (await auth.is_admin(id_)):

			data = UserDatas(
				**uARegis.dict(),
				ip_address=request.client.host,
				useragent=request.headers.get("user-agent"),
				)

			id_ = await auth.register(data=data)
			if id_:
				return {"id": id_}
			else:
				return {"data": "username уже существует"}
		else:
			return {"data":"Вы не администратор"}
	else:
		return {"data":"Вы не регистрированы"}

################