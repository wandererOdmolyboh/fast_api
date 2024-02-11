from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.shema import UserRead, UserCreate
from auth.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)