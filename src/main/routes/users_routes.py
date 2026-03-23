from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Users"])

@users_routes.post("/users")
async def create_user():
  
  return JSONResponse(
    content={"Hello": "World"},
    status_code=200
  )