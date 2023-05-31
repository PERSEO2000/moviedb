from pydantic import BaseModel

class AddMovie(BaseModel):
  img_url:str
  name:str
  url:str
  description:str