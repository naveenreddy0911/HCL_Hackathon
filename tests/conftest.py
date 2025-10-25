import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db import Base
from backend.models import user, account, kyc_documents
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DATABASE_URL)
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
        
# PYTHONPATH=$(pwd) pytest tests/ -v