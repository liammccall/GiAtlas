from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class ShapeIndex(Base):
    __tablename__ = "shape_index"
    
    shape_table: Mapped[str] = mapped_column(String, primary_key=True)
    description: Mapped[str] = mapped_column(String)