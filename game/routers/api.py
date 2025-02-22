from fastapi import APIRouter


router = APIRouter(prefix='/api')


@router.post('/users')
async def create_user():
    return
