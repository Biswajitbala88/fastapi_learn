from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines the "shape" of the data we expect
class Item(BaseModel):
    name: str
    # price: float
    # is_offer: bool = None

# A simple dictionary to act as a "database"
items = {1: "Coffee", 2: "Tea", 3: "Juice"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": items.get(item_id, "Not Found")}

@app.get("/items/")
def read_items():
    for item_id, name in items.items():
        print(f"Item ID: {item_id}, Name: {name}")
        
    return items

@app.post("/items/")
def create_item(item: Item):
    items[len(items) + 1] = item.name  # Simulate adding to the "database")
    # FastAPI has already turned the JSON into a Python object here
    return {"message": f"Created {item.name}"}

