from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, ForeignKey
from .base import Base

class Information(Base):
    __tablename__ = "informations"

    username: Mapped[str] = mapped_column(ForeignKey("users.username"), nullable=False)
    job_title: Mapped[str] = mapped_column(String(100), nullable=False)
    work_place: Mapped[str] = mapped_column(String(50), nullable=False)
    timetable: Mapped[str] = mapped_column(String(50), nullable=False)
    
    user: Mapped["User"] = relationship(back_populates="informations")