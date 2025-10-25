## These tests are generated using ChatGPT

import pytest
from backend.crud.account import create_account, get_account_by_id, get_account_by_number, get_accounts_by_user
from backend.models.user import create_test_user
from backend.schemas.account import AccountCreate
from backend.schemas.account import AccountType

# Test for creating a new account
def test_create_account(db_session):
    # Using a test user generated with create_test_user
    user = create_test_user(db_session)
    account_data = AccountCreate(account_type=AccountType.savings, pin=1234)
    account = create_account(db_session, user_id=user.id, account=account_data)

    assert account.id is not None

# Test for fetching account by ID
def test_get_account_by_id(db_session):
    user = create_test_user(db_session)
    account_data = AccountCreate(account_type=AccountType.current, pin=5678)
    created_account = create_account(db_session, user_id=user.id, account=account_data)

    fetched_account = get_account_by_id(db_session, account_id=created_account.id)
    assert fetched_account.id == created_account.id
    
# Test for fetching account by account number
def test_get_account_by_number(db_session):
    user = create_test_user(db_session)
    account_data = AccountCreate(account_type=AccountType.savings, pin=4321)
    created_account = create_account(db_session, user_id=user.id, account=account_data)

    fetched_account = get_account_by_number(db_session, account_number=created_account.account_number)
    assert fetched_account.id == created_account.id
    
# Test for fetching all accounts belonging to a specific user
def test_get_accounts_by_user(db_session):
    # Generate a test user first
    user = create_test_user(db_session)
    
    account_data1 = AccountCreate(account_type=AccountType.savings, pin=1111)
    account_data2 = AccountCreate(account_type=AccountType.current, pin=2222)
    
    # Create two accounts for the same user
    create_account(db_session, user_id=user.id, account=account_data1)
    create_account(db_session, user_id=user.id, account=account_data2)

    accounts = get_accounts_by_user(db_session, user_id=user.id)

    assert len(accounts) == 2
    account_types = {account.account_type for account in accounts}
    assert "savings" in account_types
    assert "current" in account_types
