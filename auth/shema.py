from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    login: str
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    login: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    pass
