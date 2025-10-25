from fastapi import APIRouter
from backend.routes.signin import router as signin_router
from backend.routes.signup import router as signup_router

router = APIRouter()

router.include_router(signin_router)
router.include_router(signup_router)