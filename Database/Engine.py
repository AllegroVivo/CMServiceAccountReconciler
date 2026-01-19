from __future__ import annotations

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
################################################################################

__all__ = ("SessionLocal", "init_db")

################################################################################

load_dotenv()
DB_URL = os.getenv(
    "DEV_DB_URL"
    if os.getenv("DEBUG") == "True"
    else "PROD_DB_URL",
)
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(engine, autoflush=False, expire_on_commit=False)

################################################################################
def init_db() -> None:

    from . import Models
    temp = Models.BaseModel.metadata
    temp.create_all(engine)

################################################################################
