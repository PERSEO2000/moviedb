from fastapi import FastAPI
from database import Movie
from modelos import AddMovie


app = FastAPI()

@app.post("/addmovie")
async def add_movie(movie:AddMovie):
  new_movie = Movie.create(
    img_url = movie.img_url,
    name = movie.name,
    url = movie.url,
    description = movie.description
  )
  new_movie.save()

@app.get("/movie/{id}")
async def get_movie(id:int):
  try:
    mv = Movie.get_by_id(id)
    return mv.__dict__["__data__"]
  except Movie.DoesNotExist:
    return {"not":"found"}

@app.delete("/deletemovie/{id}")
async def delete_movie(id:int):
  try:
    mv = Movie.get_by_id(id)
    mv.delete_instance()
    return {"exito":"delete is succesfull"}
  except Movie.DoesNotExist:
    return {"Error":"movie not found"}