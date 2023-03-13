from src.CoinFlip.db.base import Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class GeneralGameStatistics(Base):
    __tablename__ = "general_game_statistics"

    statistic_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id", onupdate="CASCADE"), nullable=False)
    games_won = Column(Integer, default=0, nullable=False)
    games_lost = Column(Integer, default=0, nullable=False)