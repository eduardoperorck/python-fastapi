from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.main.composer.user_finder_composer import user_finder_composer
from src.views.http_types.http_request import HttpRequest

users_routes = APIRouter(tags=["Users"])

@users_routes.post("/users")
async def create_user():
  
  return JSONResponse(
    content={"Hello": "World"},
    status_code=200
  )
  
@users_routes.get("/users/{user_name}")
async def search_users_by_name(user_name: str):
  http_request = HttpRequest(path_params={"user_name": user_name})
  user_finder = user_finder_composer()
  
  http_response = await user_finder.handle_find_user_by_name(http_request)
  return JSONResponse(
    content=http_response.body,
    status_code=http_response.status_code
  )