from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from app.core.config import settings

# create postgres url
url = URL.create(
    drivername="postgresql",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_DB,
    port=settings.DATABASE_PORT
)


engine = create_engine(url=url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)