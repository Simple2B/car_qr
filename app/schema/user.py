from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    activated: bool

    class Config:
        orm_mode = True
