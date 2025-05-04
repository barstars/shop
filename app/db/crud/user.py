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
		return data.id

	async def get_by_username(self, username):
		result = await self.session.execute(select(UsersBase).where(UsersBase.username == username))
		curr = result.scalars().first()
		return curr