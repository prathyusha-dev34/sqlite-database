from sqlalchemy.orm import Session
from app.database.models import User
from app.utils.hashing import hash_password


# Register User
def create_user(db: Session, user_data):

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get User By Email
def get_user_by_email(db: Session, email: str):

    return db.query(User).filter(
        User.email == email
    ).first()


# Get User By Username
def get_user_by_username(db: Session, username: str):

    return db.query(User).filter(
        User.username == username
    ).first()