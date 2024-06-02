# Using FastAPI to Build Python Web APIs
# https://realpython.com/fastapi-python-web-apis/

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    return {"product_id": product_id}

class ItemResponse(BaseModel):
    item_id: str

@app.get("/model/", response_model=ItemResponse)
async def read_model():
    return {"item_id": "12"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/things/")
async def create_item(item: Item):
    return item



# # main.py
# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# @app.get("/products/{product_id}")
# async def read_item(product_id: int):
#     return {"product_id": product_id}

# from pydantic import BaseModel
# class ItemResponse(BaseModel):
#     item_id: str

# @app.get("/model/", response_model=ItemResponse)
# async def root():
#     return {"item_id": "12"}


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# from typing import Optional
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# app = FastAPI()

# @app.post("/things/")
# async def create_item(item: Item):
#     return item