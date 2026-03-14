from fastapi import FastAPI, HTTPException
from trying import List
import database
import models
from models import Movie, MovieCreate

from pythonProject1.lesson22.api_development.client import response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}

@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate):
    movie_id = database.create_movie(movie)
    return models.Movie(id = movie_id, **movie.diet())

@app.get("/movies/", response_model=List[Movie])
def read_movies():
    return database.read_movies()

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def uptade_movie(movie_id, movie: MovieCreate):
    uptade = database.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return models.Movie(id=movie_id, **movie.diet())

@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie deleted successfully"}