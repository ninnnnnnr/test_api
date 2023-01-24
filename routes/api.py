from fastapi import APIRouter
from src import store_data, download_data

router = APIRouter()
router.include_router(store_data.router)
router.include_router(download_data.router)