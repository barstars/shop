from app.models.users import UserDatas, UserLogin
from app.db.crud.user import DataBaseManager

from typing import AsyncGenerator
from uuid import UUID

class Auth:
	def __init__(self, db: AsyncGenerator):
		self.dbm = DataBaseManager(session=db)

	async def auth(self, id_: str):
		print(id_)
		print(type(id_))
		print(type(UUID(id_)))
		return await self.dbm.get_by_id(UUID(id_))

	async def register(self, data: UserDatas) -> str:
		is_registered = await self.is_registered_by_name(data.username)
		if is_registered:
			return False
		else:
			user = await self.dbm.create_user(data=data)
			return str(user.id)

	async def login(self, data: UserLogin):
		login = await self.dbm.login(**(data.dict()))
		if login:
			return str(login.id)
		else:
			return None
			
	async def is_registered_by_name(self, username: str) -> bool:
		result = await self.dbm.get_by_username(username)
		if result:
			return True
		else:
			return False

	async def is_admin(self, id_:str) -> bool:
		try:
			return await self.dbm.is_admin(UUID(id_))
		except ValueError as err:
			return False