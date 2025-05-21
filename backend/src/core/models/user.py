from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String
from .base import Base

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), nullable=True)

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="user", 
        cascade="all, delete-orphan"
    )

    tasks: Mapped[list["Task"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    tasks_daily: Mapped[list["TaskDaily"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    informations: Mapped[list["Information"]] = relationship(back_populates="user", cascade="all, delete-orphan")
