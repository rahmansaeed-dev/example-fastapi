from fastapi import FastAPI
from .import models
from .database import engine
from .routers import post, user, auth , vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_username)
# print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def get_post():
    return {"message": "Hello world..."}


# @app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     return {"status" : "success"}

# DELETE A POST

# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# async def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):

#     # hashed the password 
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user =  models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id : int ,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id==id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
#     return user
    


