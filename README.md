# Initial Commitments
### Technologies: FastAPI backend, PostgreSQL database (along with SQLAlchemy ORM models), JWT Authentication (HTTPBearer or OAuth)
### UI: FastAPI Swagger UI
### Data Validation: Pydantic Schemas

## 1. User Registration & KYC
### Routes: signup, signin
### signup
Input params: name, email, password, pin, documents (aadhaar, pan)

Returns: access_token

### signin
Input params: email, password

Returns: access_token

## 2. Account creation
### Routes: create-account
### create-account
Input params: user_id, account_type, initial_deposit

Returns: account_number

## Database
### Users: id, name, email, password, pin, created at, updated at, kyc(success or failure)
### Accounts: id, user_id (foreign key), account_type, account_number, balance

---

# If time permits
### Use case 1 - Role based signup, KYC validation by admin
## 3. Money Transfer
### Routes: check-balance, deposit-money, withdraw-money, transfer-money
### check-balance
Input params: user_id, account-number, pin

Returns: current_balance

### deposit-money
Input params: user_id, account_number, amount, pin

Returns: success/failure, current_balance

### withdraw-money
Input params: user_id, account_number, amount, pin

Returns: success/failure, current_balance

### transfer-money
Input params: user_id, sender_account_number, receiver_account_number, amount, pin

Returns: success/failure, current_balance
### 7. Reporting & Dashboard
## Transactions: id, user_id (foreign key), account_id (foreign key), type (withdrawal, deposit, transfer), sender_account_number, receiver_account_number