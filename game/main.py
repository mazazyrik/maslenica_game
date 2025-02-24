from fastapi import FastAPI
from routers import api, template_routers
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='Maslenica')
app.mount('/static', StaticFiles(directory='static'), name='static')

origins = [
    'https://education-marathon.ddns.net'
    'http://194.87.216.212',
    'http://194.87.216.212:8000',
    'http://localhost:8000',
    'https://education-marathon.ddns.net',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(api.router)
app.include_router(template_routers.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
