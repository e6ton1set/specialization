# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

import enum
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
movies = []


class Genre(enum.Enum):
    ACTION = "Боевик"
    FANTASTIC = "Фантастика"
    DRAMA = "Драма"
    COMEDY = "Комедия"


class Movie(BaseModel):
    movie_id: int
    title: str
    description: str
    genre: str


class MovieIn(BaseModel):
    title: str
    description: str
    genre: str


@app.get('/movies/{genre}', response_model=list[Movie])
async def get_movies(genre: Genre) -> list[Movie]:
    result = []
    for movie in movies:
        if movie.genre == genre.value:
            result.append(movie)
    return result


@app.post('/movies/', response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(Movie(movie_id=len(movies) + 1,
                        title=new_movie.title,
                        description=new_movie.description,
                        genre=new_movie.genre)
                  )
    return movies[-1]


if __name__ == '__main__':
    uvicorn.run(
        "task_2:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
