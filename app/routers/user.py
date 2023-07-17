from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, auth2
from ..database import get_db




router = APIRouter(
    prefix="/users",
    tags=['Users']
)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session = Depends(get_db)):
    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s RETURNING *""",
    #     (id,),
    # )
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post_query.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist.",
        )
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# @router.put("/{id}",status_code=status.HTTP_201_CREATED)
# def create_user(id: int,db:Session = Depends(get_db)):
#     create_post = db.query(models.post).filter(models.post.id==id)
#     post = create_post().first()
#     db.commit()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_post(
    user_data: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    user_data = user_data.dict()
    user_data['password'] = utils.hash(user_data['password'])
    user = models.User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# UPDATE A POST
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int,updated_post : schemas.PostCreate, db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    # cursor.execute(
    #     """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #     (post.title, post.content, post.published, str(id)),
    # )
    # updated_post = cursor.fetchone()


    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found.",
        )
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return  post_query.first()


