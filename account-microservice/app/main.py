from fastapi import FastAPI
from api import account, auth
from core.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(account.router, prefix="/account", tags=["account"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "account micro service"}