from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creates a class to model an item, with three fields
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Get method that reads root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get method that returns details of an item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#Put method that updates an item given the id.
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}