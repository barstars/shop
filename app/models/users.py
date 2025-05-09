from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
from sqlalchemy import Boolean, String
from sqlalchemy.types import JSON
from pydantic import BaseModel

# DATA BASE MODELS
class UsersBase(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ip_address: Mapped[str] = mapped_column(String)
    useragent: Mapped[str] = mapped_column(String)
    setting: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    password: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, unique=True)

#########################


# pydantic.BaseModel MODELS
class UserRegister(BaseModel):
	password: str
	email: str
	username: str

class UserDatas(UserRegister):
    ip_address: str
    useragent: str
    setting: Optional[dict] = None
    is_admin: Optional[bool] = None

class UserLogin(BaseModel):
    password: str
    username: str

#########################