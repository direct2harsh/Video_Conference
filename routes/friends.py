from fastapi.routing import APIRouter


router = APIRouter(prefix="/friends",tags=["Friends"])

@router.get("/")
async def friends():
    return "Friends router is working fine"


# send friend request

# Accept friend request

# List all Friends of user 

# Block friend

