from fastapi import FastAPI
from typing import Union
from app_api.xtrafiles.local_repository import LocalDictRepository
from app_api.xtrafiles.property import Property, RealEstateSite
from pydantic import BaseModel

app = FastAPI()
repo =  LocalDictRepository()


# this decorator tells FastAPI that the function below corresponds to the path / with an operation get 
# pass here the ath parameters
@app.get("/") 
# as the query parameters if needed, they are optional
def index():
    return {"Hello World"}


@app.post("/create_property")
def create_property(property: Property): # create
    created_property = repo.create_property(property)
    return created_property

@app.delete("/delete_property") # delete
def delete_property(property_id: str):
    deleted_property = repo.delete_property(property_id)
    

@app.get("/retireve_properties")   # read
def get_property(property_id: str):
    get_property = repo.get_property(property_id)
    return get_property

@app.put("/update_properties")   # update
def update_property(property: Property):
    update_property = repo.update_property(property)
    return update_property

@app.get("/reduced_properties")   # reduced read
def get_reduced_property(property_id: str):
    get_reduced_property = repo.get_reduced_property(property_id)
    return get_reduced_property