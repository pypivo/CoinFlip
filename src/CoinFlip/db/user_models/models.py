from src.CoinFlip.db.base import Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    nick_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)