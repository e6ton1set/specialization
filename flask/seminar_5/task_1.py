# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
tasks = []


class Task(BaseModel):
    task_id: int
    title: str
    description: Optional[str] = None
    status: Optional[bool] = None


class TaskIn(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[bool] = None


@app.get('/tasks/', response_model=list[Task])
async def get_list_tasks():
    return tasks


@app.post('/tasks/', response_model=list[Task])
async def create_task(new_task: TaskIn):
    tasks.append(Task(task_id=len(tasks) + 1,
                      title=new_task.title,
                      description=new_task.description,
                      status=new_task.status))
    return tasks


@app.put('/tasks/', response_model=Task)
async def edit_task(new_task: TaskIn, task_id: int):
    for i in range(0, len(tasks)):
        if tasks[i].task_id == task_id:
            current_task = tasks[task_id - 1]
            current_task.title = new_task.title
            current_task.description = new_task.description
            current_task.status = new_task.status
            return current_task
    raise HTTPException(status_code=404, detail="Задача не найдена.")



@app.delete('/tasks/', response_model=dict)
async def edit_task(task_id: int):
    for i in range(0, len(tasks)):
        if tasks[i].task_id == task_id:
            tasks.remove(tasks[i])
            return {"message": f"the task ID {task_id} was successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Задача не найдена.")


if __name__ == '__main__':
    uvicorn.run(
        "task_1:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
