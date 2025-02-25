from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import User as UserModel


class User(BaseModel):
    username: str
    score: int


class UserAll(BaseModel):
    id: int
    username: str
    score: int


class Score(BaseModel):
    score: int


router = APIRouter(prefix='/api')


@router.get('/users/top')
def get_top_users():
    users = list(UserModel.select())
    sorted_users = sorted(users, key=lambda user: int(
        user.score), reverse=True)

    result = [
        {"rank": i + 1, "username": user.username, "score": int(user.score)}
        for i, user in enumerate(sorted_users[:10])
    ]

    return result


@router.post('/users')
async def create_user(user: User):
    if UserModel.select().where(UserModel.username == user.username).exists():
        raise HTTPException(
            status_code=400, detail='Пользователь уже существует')
    UserModel.create(username=user.username, score=user.score)
    return {'username': user.username, 'score': user.score}


@router.get('/users/{username}')
async def get_user(username: str):
    if UserModel.select().where(UserModel.username == username).exists():
        user = UserModel.select().where(UserModel.username == username).get()
        return {'username': user.username, 'score': user.score}
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@router.put('/users/{username}')
async def update_user(username: str, score: Score):
    if UserModel.select().where(UserModel.username == username).exists():
        UserModel.update(username=username, score=score.score).where(
            UserModel.username == username).execute()
        return {'username': username, 'score': score.score}
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@router.delete('/users/{username}')
async def delete_user(username: str):
    if UserModel.select().where(UserModel.username == username).exists():
        UserModel.delete().where(UserModel.username == username).execute()
        return {'message': 'Пользователь удален'}
    raise HTTPException(status_code=404, detail='Пользователь не найден')


@router.get('/users', response_class=UserAll)
async def get_users():
    users = UserModel.select()
    return [{'username': user.username, 'score': user.score} for user in users]


@router.patch('/users/{username}')
async def update_user_score(username: str, score: Score):
    if UserModel.select().where(UserModel.username == username).exists():
        UserModel.update(username=username, score=score.score).where(
            UserModel.username == username).execute()
        return {'username': username, 'score': score.score}
    raise HTTPException(status_code=404, detail='Пользователь не найден')
