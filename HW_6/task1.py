# Задание №1
# Разработать API для управления списком пользователей с
# использованием базы данных SQLite. Для этого создайте
# from dataclasses import Field
# модель User со следующими полями:
# ○ id: int (идентификатор пользователя, генерируется автоматически)
# ○ username: str (имя пользователя)
# ○ email: str (электронная почта пользователя)
# ○ password: str (пароль пользователя)

# API должно поддерживать следующие операции:
# ○ Получение списка всех пользователей: GET /users/
# ○ Получение информации о конкретном пользователе: GET /users/{user_id}/
# ○ Создание нового пользователя: POST /users/
# ○ Обновление информации о пользователе: PUT /users/{user_id}/
# ○ Удаление пользователя: DELETE /users/{user_id}/
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from pathlib import Path
from typing import List
import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///db.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("username", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(128)),
                         )
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class UserIn(BaseModel):
    """Размеры значений изменяются тут"""
    username: str = Field(min_length=1, max_length=12, unique=True)
    email: str = Field(min_length=5, max_length=50, )
    password: str = Field(min_length=8, max_length=64, )


class Users(UserIn):
    id: int


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def get_all_users():
    return 'hello world'


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(username=f'user{i}', email=f'mail{i}@mail.ru', password='change_me')
        await database.execute(query)
    return {'message': f'{count} fake users created'}


@app.get('/users/', response_model=List[Users])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}/', response_model=Users)
async def get_user_id(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post('/user/add', response_model=Users)
async def create_user(user: UserIn):
    q = users.insert().values(username=user.username, email=user.email, password=user.password)
    last_record_id = await database.execute(q)
    return {**user.model_dump(), "id": last_record_id}


@app.put('/user/update/{user_id}', response_model=Users)
async def update_user(user: UserIn, user_id: int):
    q = users.update().where(users.c.id == user_id).values(username=user.username, email=user.email,
                                                           password=user.password)
    await database.execute(q)
    return {**user.model_dump(), "id": user_id}


@app.delete('/user/del/{user_id}/')
async def delete_user(user_id: int):
    q = users.delete().where(users.c.id == user_id)
    await database.execute(q)
    return {'mgs': f'User deleted {user_id}'}


if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", port=8001)
