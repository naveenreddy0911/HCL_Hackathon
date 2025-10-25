## These tests are generated using ChatGPT

import pytest
from backend.models.user import create_test_user
from backend.models.kyc_documents import KYC_Documents

# Test for creating KYC documents for a user
def test_create_kyc_documents(db_session):
    user = create_test_user(db_session)
    
    # Sample binary data for testing
    aadhaar_data = b"dummy_aadhaar_content"
    pan_data = b"dummy_pan_content"
    
    kyc_doc = KYC_Documents(
        user_id=user.id,
        aadhaar=aadhaar_data,
        pan=pan_data
    )
    
    db_session.add(kyc_doc)
    db_session.commit()
    db_session.refresh(kyc_doc)
    
    assert kyc_doc.user_id == user.id
    assert kyc_doc.aadhaar == aadhaar_data
    assert kyc_doc.pan == pan_data
    assert kyc_doc.uploaded_at is not None

# Test for fetching KYC documents by user_id
def test_get_kyc_documents_by_user(db_session):
    user = create_test_user(db_session)
    
    kyc_doc = KYC_Documents(
        user_id=user.id,
        aadhaar=b"aadhaar_test",
        pan=b"pan_test"
    )
    
    db_session.add(kyc_doc)
    db_session.commit()
    
    fetched_kyc = db_session.query(KYC_Documents).filter_by(user_id=user.id).first()
    assert fetched_kyc is not None
    assert fetched_kyc.user_id == user.id
    assert fetched_kyc.aadhaar == b"aadhaar_test"
    assert fetched_kyc.pan == b"pan_test"
