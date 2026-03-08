from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    experiences = relationship("Experience", back_populates="user")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    location = Column(String)

    experiences = relationship("Experience", back_populates="company")


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True)

    title = Column(String)
    description = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    user = relationship("User", back_populates="experiences")
    company = relationship("Company", back_populates="experiences")