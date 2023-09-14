# Задание №3
# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


app = FastAPI()
users = []


class User(BaseModel):
    user_id: int
    name: str
    email: str
    password: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


@app.get("/users/", response_model=list[User])
async def get_users():
    return users


@app.post("/users/", response_model=list[User])
async def add_user(new_user: UserIn):
    users.append(User(user_id=len(users) + 1,
                      name=new_user.name,
                      email=new_user.email,
                      password=hash_password(new_user.password)
                      )
                 )
    return users


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
