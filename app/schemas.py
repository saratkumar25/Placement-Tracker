from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class CompanyCreate(BaseModel):
    name: str
    location: str


class ExperienceCreate(BaseModel):
    title: str
    description: str
    company_id: int