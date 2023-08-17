from typing import Any, Dict, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session

from app.repository.base_crud import CRUDBase
from app.src.models.user import User
from app.src.schemas.user import UserCreate, UserUpdate



class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
   
    def get_by_uuid(self, db: Session, *, uuid: UUID) -> Optional[User]:
        return db.query(User).filter(User.uuid == uuid).first()

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)