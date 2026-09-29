from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey
from .database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255))
    password_hash = Column(String(255))
    role = Column(String(30))


class Category(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)


class Event(Base):
    __tablename__ = "Events"

    id = Column(Integer, primary_key=True)
    organizer_id = Column(Integer, ForeignKey("Users.id"))
    category_id = Column(Integer, ForeignKey("Categories.id"))

    title = Column(String(255))
    description = Column(Text)

    start_datetime = Column(DateTime)
    end_datetime = Column(DateTime)

    location = Column(String(255))
    image_url = Column(String(500))

    price = Column(Numeric(10, 2))
    max_participants = Column(Integer)