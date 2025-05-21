from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base

class TaskDaily(Base):
    __tablename__ = "tasks_daily"

    username: Mapped[int] = mapped_column(ForeignKey("users.username"))
    description: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="tasks_daily")
