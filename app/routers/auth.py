# from fastapi import Depends, status, HTTPException,APIRouter,Response
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session


# from ..import database, schemas, models, utils, auth2

# router = APIRouter(tags=['Authentication'])



# @router.post('/login', response_model=schemas.token)
# def login(user_credentials: OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
#     user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail=f"Invalid credentials.")

#     if not utils.verify(user_credentials.password,user.password):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail=f"Invalid creadetials.")


#     access_token = auth2.create_access_token(data={"user_id":user.id})
#     return {"access_token": access_token,"token_type":"bearer"}




from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, auth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials.")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials.")

    access_token = auth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}







