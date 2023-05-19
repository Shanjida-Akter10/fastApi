from typing import Union
from fastapi import FastAPI
import random as rd
app = FastAPI()
items = {
    "1": {"name": "Foo", "price": 50.2},
    "2": {"name": "Bar", "price": 62},
    "3": {"name": "Baz", "price": 50.8},
    "4": {"name": "Too", "price": 54.3},
    "5": {"name": "Boo", "price": 20.6},
}
@app.get("/")
def read_root():
    return {"Hello from FastAPI"} 

# endpoint in postman: http://localhost:5000/item
@app.get("/item")
async def read_item():
    random_key = rd.choice(list(items.keys())) ## randomly selecting a key in items
    random_value = items[random_key]  ## calling the value of the selected key
    return {"message": random_value}  ## returning the value

# endpoint in postman: http://localhost:5000/items 
@app.get("/items")
async def read_items():
    return items     ## returning all the value

# start the app → uvicorn index:app --port 5000 --reload --log-level debug
#task02 done
    