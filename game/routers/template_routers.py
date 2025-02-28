from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


# @router.get('/', response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse('index.html', {'request': request})


@router.get('/', response_class=HTMLResponse)
async def final(request: Request):
    return templates.TemplateResponse('final.html', {'request': request})


@router.get('/leaderboard', response_class=HTMLResponse)
async def leaderboard(request: Request):
    return templates.TemplateResponse('rate.html', {'request': request})


@router.get('/settings', response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse('settings.html', {'request': request})
