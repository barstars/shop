from app.models.users import UserDatas, UserLogin
from app.db.crud.user import DataBaseManager

from typing import AsyncGenerator

class Auth:
	def __init__(self, db: AsyncGenerator):
		self.dbm = DataBaseManager(session=db)

	async def register(self, data: UserDatas) -> str:
		is_registered = await self.is_registered_by_name(data.username)
		if is_registered:
			return False
		else:
			return await self.dbm.create_user(data=data)

	async def login(self, data: UserLogin):
		login = await self.dbm.login(**(data.dict()))
		if login:
			return login.id
		else:
			return None
			
	async def is_registered_by_name(self, username) -> bool:
		result = await self.dbm.get_by_username(username)
		if result:
			return True
		else:
			return False