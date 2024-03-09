from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import httpx


router = APIRouter()



userInfo = {"username":"ashish", "password":"saxena"}
clientUrl = "https://randomuser.me/api/"


# Endpoint with basic authentication
@router.get("/user")
async def get_random_user(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    if credentials.username != userInfo['username'] or credentials.password != userInfo['password']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )

    # Connect and fetch the data from random user API 
    async with httpx.AsyncClient() as client:
        response = await client.get(clientUrl)
        if response.status_code != 200:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            	detail="External service error")
        user_data = response.json()["results"][0]

        return user_data