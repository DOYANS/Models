"""
models API
"""

from fastapi import APIRouter

router = APIRouter(
    # prefix="/api",
    # tags="[api]",
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description":"Not Found."}},
)

router.get('/', tags=['data'])
async def data():
    """ prediction. """
    return 0
