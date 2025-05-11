from fastapi import APIRouter, Depends, Response, Cookie
from fastapi.responses import FileResponse

from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="/admin",
	tags=["admin"])

@router.get("/register")
async def register(db: AsyncGenerator = Depends(get_db),
					cookies_data: str = Cookie(default="{}")):
	
	cookies = json.loads(cookies_data)
	if cookies:
		id_ = cookies.get("id")
		auth = Auth(db)
		if (await auth.is_admin(id_)):
			return FileResponse("frontend/admin/register/index.html")
		else:
			return {"data":"Вы не администратор"}
	else:
		return {"data":"Вы не регистрированы"}