from fastapi import FastAPI
from routers import api, template_routers
from fastapi.staticfiles import StaticFiles


app = FastAPI(title='Maslenica')
app.mount('/static', StaticFiles(directory='static'), name='static')


app.include_router(api.router)
app.include_router(template_routers.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
