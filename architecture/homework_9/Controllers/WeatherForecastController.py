import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.post('/add-data/', status_code=200)
async def add():
    pass


@app.put('/update-data/', status_code=200)
async def update():
    pass


@app.delete('/delete-data/', status_code=200)
async def delete():
    pass


@app.get('/get-data/', status_code=200)
async def get():
    pass


if __name__ == '__main__':
    uvicorn.run(
        "WeatherForecastController:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )


