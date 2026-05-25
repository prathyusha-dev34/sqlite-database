from sqlalchemy.orm import Session
from app.database.models import Movie


# Get All Movies
def get_all_movies(db: Session):

    return db.query(Movie).all()


# Get Single Movie
def get_movie_by_id(db: Session, movie_id: int):

    return db.query(Movie).filter(
        Movie.id == movie_id
    ).first()


# Get Movie By Title
def get_movie_by_title(db: Session, title: str):

    return db.query(Movie).filter(
        Movie.title == title
    ).first()


# Create Movie
def create_movie(db: Session, movie_data):

    new_movie = Movie(
        title=movie_data.title,
        genre=movie_data.genre,
        rating=movie_data.rating,
        image=movie_data.image
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


# Update Movie
def update_movie(db: Session, movie_id: int, movie_data):

    movie = get_movie_by_id(db, movie_id)

    if movie:
        movie.title = movie_data.title
        movie.genre = movie_data.genre
        movie.rating = movie_data.rating
        movie.image = movie_data.image

        db.commit()
        db.refresh(movie)

    return movie


# Delete Movie
def delete_movie(db: Session, movie_id: int):

    movie = get_movie_by_id(db, movie_id)

    if movie:
        db.delete(movie)
        db.commit()

    return movie