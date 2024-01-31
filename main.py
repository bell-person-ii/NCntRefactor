from fastapi import FastAPI , Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from time import strftime
from random import randrange
from database.repository import PeopleCountRepository
import asyncio


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

status = {"people_count": -1, "analysis_time": strftime('%Y-%m-%d %H:%M:%S')}

async def make_and_test_data():
    while True:
        status["people_count"]= randrange(1,10)
        status["analysis_time"]= strftime('%Y-%m-%d %H:%M:%S')
        print(status)
        save_people_count()
        await asyncio.sleep(2)

def save_people_count():
    PeopleCountRepository.createPeopleCount(status["people_count"], status["analysis_time"])


@app.on_event("startup")
async def start_polling():
    asyncio.create_task(make_and_test_data())


@app.get("/main")
async def name(request: Request):
    info = PeopleCountRepository.findRecentOne()
    response = {"time":info.time,"head_count":info.head_count}
    context = {"request":request,"response":response}
    return  templates.TemplateResponse("main.html",context)
