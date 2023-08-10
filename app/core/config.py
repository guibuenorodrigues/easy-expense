from pydantic import AnyHttpUrl, EmailStr, field_validator
from pydantic_settings import BaseSettings
from typing import List, Union
from dotenv import find_dotenv

class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # got from internet, but needs to be evaluated the reason to use
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    FIRST_SUPERUSER: EmailStr = "admin@easyexpense.com"


    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    DATABASE_PORT: int


    class Config:
        case_sensitive = True
        env_file = find_dotenv(filename='.env')
        

settings = Settings()