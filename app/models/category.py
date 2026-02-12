from pydantic import BaseModel

class Category(BaseModel):
    id_categoria:int
    nome_categoria:str
    
    