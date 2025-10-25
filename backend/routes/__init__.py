from fastapi import APIRouter
from backend.routes.signin import router as signin_router
from backend.routes.signup import router as signup_router
from backend.routes.kyc_upload import router as kyc_upload_router
from backend.routes.kyc_status import router as kyc_status_router
from backend.routes.create_account import router as create_account_router
from backend.routes.get_user_accounts import router as get_user_accounts_router
from backend.routes.check_account_balance import router as check_account_balance_router

router = APIRouter()

router.include_router(signin_router)
router.include_router(signup_router)
router.include_router(kyc_upload_router)
router.include_router(kyc_status_router)
router.include_router(create_account_router)
router.include_router(get_user_accounts_router)
router.include_router(check_account_balance_router)