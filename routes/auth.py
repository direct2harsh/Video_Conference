from fastapi.routing import APIRouter


router = APIRouter(prefix="/auth",tags=["Auth"])

@router.get("/")
async def auth():
    return "Auth Router working fine"

# Login user

# Logout user

