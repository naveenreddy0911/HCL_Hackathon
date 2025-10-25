from fastapi import APIRouter
from backend.routes.signin import router as signin_router
from backend.routes.signup import router as signup_router
from backend.routes.kyc_upload import router as kyc_upload_router
from backend.routes.kyc_status import router as kyc_status_router

router = APIRouter()

router.include_router(signin_router)
router.include_router(signup_router)
router.include_router(kyc_upload_router)
router.include_router(kyc_status_router)