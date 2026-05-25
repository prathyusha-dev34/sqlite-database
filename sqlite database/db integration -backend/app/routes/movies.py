from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Movie
from app.schemas.movie_schema import MovieCreate


router = APIRouter()


# GET all movies
@router.get("/movies")
def get_movies(db: Session = Depends(get_db)):

    movies = db.query(Movie).all()

    return movies


# ADD movie
@router.post("/movies")
def add_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db)
):

    # duplicate check
    existing_movie = db.query(Movie).filter(
        Movie.title == movie.title
    ).first()

    if existing_movie:
        raise HTTPException(
            status_code=400,
            detail="Movie already exists"
        )

    new_movie = Movie(
        title=movie.title,
        genre=movie.genre,
        rating=movie.rating,
        image=movie.image
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return {
        "message": "Movie added successfully",
        "movie": new_movie
    }


# UPDATE movie
@router.put("/movies/{movie_id}")
def update_movie(
    movie_id: int,
    movie: MovieCreate,
    db: Session = Depends(get_db)
):

    existing_movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not existing_movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    existing_movie.title = movie.title
    existing_movie.genre = movie.genre
    existing_movie.rating = movie.rating
    existing_movie.image = movie.image

    db.commit()
    db.refresh(existing_movie)

    return {
        "message": "Movie updated successfully",
        "movie": existing_movie
    }


# DELETE movie
@router.delete("/movies/{movie_id}")
def delete_movie(
    movie_id: int,
    db: Session = Depends(get_db)
):

    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    db.delete(movie)
    db.commit()

    return {
        "message": "Movie deleted successfully"
    }