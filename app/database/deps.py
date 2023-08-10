from typing import Generator
from app.database.session import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()