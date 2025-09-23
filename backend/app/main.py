# backend/app/main.py
from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.orm import Session
from . import models, database, schemas, crud, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Docker & Postgres!"}

@app.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user



@app.post("/login", response_model=schemas.Token)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, request.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not crud.verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = auth.create_access_token({"sub": user.username})
    refresh_token = auth.create_refresh_token({"sub": user.username})

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}



@app.post("/refresh")
def refresh_token(request: schemas.RefreshRequest):
    new_access_token = auth.refresh_access_token(request.refresh_token)
    if not new_access_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    return {"access_token": new_access_token, "token_type": "bearer"}







