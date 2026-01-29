from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import Integer, String, Date, DateTime, Text, Boolean, ForeignKey, SmallInteger, Numeric, Table, Column
from typing import Optional, List
from datetime import date, datetime
from enum import Enum as PyEnum
from passlib.hash import bcrypt


class Base(DeclarativeBase):
    pass


class UserRoleChoice(str, PyEnum):
    client = 'client'
    owner = 'owner'




class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String)
    photo: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    age: Mapped[Optional[int]] = mapped_column(SmallInteger, nullable=True)
    phone_number: Mapped[str| None] = mapped_column(String, nullable=True)
    user_role: Mapped[UserRoleChoice] = mapped_column(String(16), default=UserRoleChoice.client)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True)
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates="token_user", cascade="all, delete-orphan")

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'




class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_profiles.id"))
    token_user: Mapped["UserProfile"] = relationship(UserProfile,back_populates="user_token")
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.token}'
