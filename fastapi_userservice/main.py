
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(id=UUID("845ab787-d6f8-4bf2-a301-6d5bde757117"), first_name="Raju", last_name="Guruswamy",
         gender=Gender.male, roles=[Role.admin, Role.user]),
    User(id=UUID("f5c916bd-2fdf-492e-af93-e7d71377cab8"), first_name="Alex", last_name="Jones",
         gender=Gender.male, roles=[Role.student])
]


@app.get("/")
def root():
    return {"Hello", "World"}


@app.get("/api/v1/users")
async def list_users():
    return db


@app.get("/api/v1/users/{id}")
async def get_user_by_id(id: UUID):
    # Search for the user in the in-memory database
    for user in db:
        if user.id == id:
            return user
    # If user not found, raise a 404 error
    raise HTTPException(
        status_code=404, detail=f"User with id {id } not found")


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):

    for user in db:
        if user.id == id:
            db.remove(user)
            return {"detail": "User deleted successfully"}

    raise HTTPException(
        status_code=404, detail=f"User with id {id } does not exist")


@app.put("/api/v1/users/{id}")
async def update_user(update_user: UserUpdateRequest, id: UUID):
    for user in db:
        if user.id == id:
            if update_user.first_name is not None:
                user.first_name = update_user.first_name
            if update_user.last_name is not None:
                user.last_name = update_user.last_name
            if update_user.middle_name is not None:
                user.middle_name = update_user.middle_name
            if update_user.roles is not None:
                user.roles = update_user.roles
            return {"detail": f"User with id {id } updated successfully"}
    raise HTTPException(
        status_code=404, detail=f"User with id {id } does not exist")
