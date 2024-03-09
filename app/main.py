from fastapi import FastAPI
from fastapi import  status
#from .internal import admin (if any admin route does exist)
from .routers import users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Allow all origins, methods, and headers in development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)



# Health check endpoint without authentication or Applicaton liveness 
@app.get("/health")
async def liveness():
    return {"Application Health Status": status.HTTP_200_OK,"status": status.HTTP_200_OK}




