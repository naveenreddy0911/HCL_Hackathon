## These tests are generated using ChatGPT

import pytest
from backend.models.user import User, create_test_user

def test_create_user(db_session):
    # Create a test user
    user = create_test_user(db_session, name="Alice", email="alice@example.com")
    
    assert user.id is not None
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.kyc_status == "pending"

def test_user_unique_email(db_session):
    # Create first user
    create_test_user(db_session, name="Bob", email="bob@example.com")
    
    # Attempt to create a second user with the same email should fail
    with pytest.raises(Exception):
        create_test_user(db_session, name="Bob2", email="bob@example.com")

def test_user_relationships(db_session):
    # Create a user
    user = create_test_user(db_session)
    
    # Initially, user should have no accounts or KYC documents
    assert user.accounts == []
    assert user.kyc_documents == []

def test_get_user_by_email(db_session):
    # Create user
    create_test_user(db_session, name="Charlie", email="charlie@example.com")
    
    # Fetch user manually
    user = db_session.query(User).filter(User.email == "charlie@example.com").first()
    
    assert user is not None
    assert user.name == "Charlie"
