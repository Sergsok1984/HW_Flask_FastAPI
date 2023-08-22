# Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja
# для динамического формирования HTML-страницы.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы,
# таблицу со списком пользователей и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, Request, Form
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class UserIn(BaseModel):
    name: str
    email: Optional[str]
    password: str


class User(UserIn):
    id: int


users = [
    User(id=1, name='user_1', email='1@mail.ru', password='pas_1'),
    User(id=2, name='user_2', email='2@mail.ru', password='pas_2'),
    User(id=3, name='user_3', email='3@mail.ru', password='pas_3')
]


@app.get("/", response_model=list[User], summary='Получить список пользователей', tags=['Получить'])
async def get_users():
    return users


@app.get("/get_html", response_class=HTMLResponse, summary='Получить html-шаблон', tags=['Получить'])
async def get_html(request: Request):
    title = 'Список пользователей'
    return templates.TemplateResponse('main.html', {'request': request, 'title': title, 'users': users})


@app.post('/get_html', summary='Добавить нового пользователя (форма)', tags=['Добавить'])
async def add_new_user(request: Request, name=Form(), email=Form(), password=Form()):
    users.append(
        User(
            id=len(users) + 1,
            name=name,
            email=email,
            password=password
        )
    )
    title = 'Список пользователей'
    return templates.TemplateResponse('main.html', {'request': request, 'title': title, 'users': users})


@app.post("/user/", response_model=User, summary='Добавить нового пользователя', tags=['Добавить'])
async def add_user(item: UserIn):
    id = len(users) + 1
    user = User
    user.id = id
    user.name = item.name
    user.email = item.email
    user.password = item.password
    users.append(user)
    return users


@app.put("/user/{id}", response_model=User, summary='Изменить данные существующего пользователя', tags=['Изменить'])
async def put_user_by_id(id: int, changed_user: UserIn):
    user = check_user_exist(id)
    user.name = changed_user.name
    user.email = changed_user.email
    user.password = changed_user.password
    return user


def check_user_exist(id):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail=f'User with {id = } not found')


@app.get("/user/{id}", response_model=User, summary='Получить пользователя по id', tags=['Получить'])
async def get_user_by_id(id: int):
    return check_user_exist(id)


@app.delete("/user/{id}", summary='Удалить пользователя по id', tags=['Удалить'])
async def delete_user(id: int):
    users.remove(check_user_exist(id))
    return users


if __name__ == '__main__':
    uvicorn.run(
        "HW_5.task:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
