from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String
from .base import Base

class Admin(Base):
    __tablename__ = "admins"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), nullable=True)
    password: Mapped[str | None] = mapped_column(String(100), nullable=True)