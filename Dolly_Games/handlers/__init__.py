from aiogram import Router

from .me import router as me_router
from .rp_dolly import router as rp_dolly_router
from .start_help import router as start_help_router
from .test import router as test_router

router = Router(name="handlers_router")
router.include_routers(
    me_router,
    rp_dolly_router,
    start_help_router,
    test_router,
)
