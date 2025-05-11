from app.models.users import UsersBase, UserDatas

from sqlalchemy import select

from typing import AsyncGenerator

class DataBaseManager:
	def __init__(self, session: AsyncGenerator):
		self.session = session

	async def create_user(self, data: UserDatas):
		data = UsersBase(**data.dict())
		self.session.add(data)
		await self.session.commit()
		return data

	async def get_by_username(self, username):
		result = await self.session.execute(select(UsersBase).where(UsersBase.username == username))
		curr = result.scalars().first()
		return curr

	async def login(self, username, password):
		result = await self.session.execute(select(UsersBase).where((UsersBase.username == username) and (UsersBase.password == password)))
		curr = result.scalars().first()
		return curr

	async def get_by_id(self, id_):
		result = await self.session.execute(select(UsersBase).where(UsersBase.id == id_))
		curr = result.scalars().first()
		return curr

	async def is_admin(self, id_):
		result = await self.session.execute(select(UsersBase).where((UsersBase.id == id_) and (UsersBase.is_admin == True)))
		curr = result.scalars().first()
		if curr:
			return True
		else:
			return False