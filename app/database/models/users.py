# models/users.py
# Since I have defined the basic credentials in files, it is not being used. We can use it when we target from the database.

from pydantic import BaseModel

class UserAuth(BaseModel):
    username: str
    password: str
