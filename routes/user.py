
from fastapi.routing import APIRouter


router = APIRouter(prefix='/user',tags=["User"])

# chek the user router is working fine
@router.get("/")
async def getUser():
    return "User router is working fine"


# Create user


# update user/ change password and other details

# Delete user


# Get details of user

# check userId already exist

