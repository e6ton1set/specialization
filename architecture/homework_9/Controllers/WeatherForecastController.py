from datetime import datetime
from http.client import HTTPException
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data_weather = []


class WeatherForecast(BaseModel):
    weather_id: int
    date: datetime
    temperatureC: float
    temperatureF: Optional[float] = None


class WeatherForecastIn(BaseModel):
    date: datetime
    temperatureC: float
    temperatureF: float


@app.post('/add-data/', status_code=200, response_model=list[WeatherForecast])
async def add_weather(new_weather: WeatherForecastIn):
    data_weather.append(WeatherForecast(weather_id=len(data_weather) + 1,
                                        date=new_weather.date,
                                        temperatureC=new_weather.temperatureC,
                                        temperatureF=new_weather.temperatureF))
    return data_weather


@app.put('/update-data/', status_code=200, response_model=WeatherForecast)
async def update_weather(new_weather: WeatherForecastIn, weather_id: int):
    for i in range(0, len(data_weather)):
        if data_weather[i].weather_id == weather_id:
            current_weather = data_weather[weather_id - 1]
            current_weather.date = new_weather.date
            current_weather.temperatureC = new_weather.temperatureC
            current_weather.temperatureF = new_weather.temperatureF
            return current_weather
    raise HTTPException(status_code=404, detail="Запись не найдена.")


@app.delete('/delete-data/', response_model=dict)
async def delete_weather(weather_id: int):
    for i in range(0, len(data_weather)):
        if data_weather[i].weather_id == weather_id:
            data_weather.remove(data_weather[i])
            return {"message": f"the weather ID {weather_id} was successfully deleted"}
    raise HTTPException(status_code=404, detail="Запись не найдена.")


@app.get('/get-data/', status_code=200, response_model=list[WeatherForecast])
async def get_weather():
    return data_weather


if __name__ == '__main__':
    uvicorn.run(
        "WeatherForecastController:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
