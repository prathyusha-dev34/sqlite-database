from pydantic import BaseModel


# Create Movie Schema
class MovieCreate(BaseModel):
    title: str
    genre: str
    rating: str
    image: str


# Update Movie Schema
class MovieUpdate(BaseModel):
    title: str
    genre: str
    rating: str
    image: str


# Response Schema
class MovieResponse(BaseModel):
    id: int
    title: str
    genre: str
    rating: str
    image: str

    class Config:
        orm_mode = True