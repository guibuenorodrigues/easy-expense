from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID
from typing import Optional

from app.core.config import settings
from app.src.schemas.user import UserCreate, UserUpdate, UserSearchResults, UserSchema
from app.database.deps import get_db
from app import repository

router = APIRouter(prefix=f"{settings.API_V1}/users", tags=["users"])


@router.get("/", status_code=200, response_model=UserSearchResults)
async def search(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="my name"),
    max_results: Optional[int] = 10,
    db: Session = Depends(get_db),
):
    users = repository.user.get_multi(db=db, limit=max_results)

    if not users:
        raise HTTPException(status_code=404, detail=f"there are no users registered")

    response = UserSearchResults()

    if not keyword:
        response.results = users
        return response

    results = filter(lambda user: keyword.lower() in user.label.lower(), users)

    response.results = results
    return response


@router.get("/{unique_id}", status_code=200, response_model=UserSearchResults)
async def retrieve_by_id(*, unique_id: UUID, db: Session = Depends(get_db)):
    result = repository.user.get_by_uuid(db=db, uuid=unique_id)

    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with ID {unique_id} not found"
        )

    return result


@router.get("/email/{email}", status_code=200, response_model=UserSearchResults)
async def retrieve_by_email(*, email: str, db: Session = Depends(get_db)):
    result = repository.user.get_by_email(db=db, email=email)

    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with EMAIL {email} not found"
        )

    return result


@router.post("/", status_code=201, response_model=UserSchema)
async def create(*, user_create: UserCreate, db: Session = Depends(get_db)):
    try:
        result = repository.user.create(db=db, obj_in=user_create)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{e}")
    
    return result


@router.put("/{unique_id}", status_code=201, response_model=UserSchema)
async def update(
    *, unique_id: int, user_update: UserUpdate, db: Session = Depends(get_db)
):
    return {"msg": f"user {unique_id} updated"}


@router.delete("/{unique_id}", status_code=200)
async def remove(*, unique_id: int, db: Session = Depends(get_db)):
    repository.user.remove(db=db, id=unique_id)
    
    return {"msg": f"user {unique_id} deleted"}
