from fastapi import APIRouter, Depends, Request, Cookie, Response

from app.db.session import get_db
from app.services.auth import Auth

import json
from typing import AsyncGenerator

router = APIRouter(
	prefix="",
	tags=["home"])

@router.get("/")
async def home(request: Request,
						db: AsyncGenerator = Depends(get_db),
						cookies_data: str = Cookie(default="{}")):
	cookies = json.loads(cookies_data)
	return cookies