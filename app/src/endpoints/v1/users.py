from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID
from typing import Optional

from app.core.config import settings
from app.src.schemas.user import UserCreate, UserUpdate, UserSearchResults, UserSchema
from app.database.deps import get_db
from app import repository as repo

router = APIRouter(prefix=f"{settings.API_V1}/users", tags=["users"])


@router.get("/", status_code=200, response_model=UserSearchResults)
async def retrieve_all(
    skip: int = Query(0, ge=0),
    max_results: int = Query(100, gt=0),
    db: Session = Depends(get_db),
):
    users = repo.user.get_multi(db=db, skip=skip, limit=max_results)

    if not users:
        raise HTTPException(status_code=404, detail=f"there are no users registered")

    response = UserSearchResults()
    response.results = users

    return response

     
@router.get("/{unique_id}", status_code=200, response_model=UserSearchResults)
async def retrieve_by_id(*, unique_id: UUID, db: Session = Depends(get_db)):
    result = repo.user.get_by_uuid(db=db, uuid=unique_id)
    print(result)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User with ID {unique_id} not found"
        )
    
    response = UserSearchResults()
    response.results = [result]
    return Response(content=response.model_dump_json(), status_code=status.HTTP_200_OK)


@router.post("/", status_code=201, response_model=UserSchema)
async def create(*, user_create: UserCreate, db: Session = Depends(get_db)):
    try:
        result = repo.user.create(db=db, obj_in=user_create)
    except IntegrityError as sql:
        return Response(content=user_create.model_dump_json(), status_code=status.HTTP_409_CONFLICT)
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
    repo.user.remove(db=db, id=unique_id)
    
    return {"msg": f"user {unique_id} deleted"}
