from fastapi import FastAPI
from models.non_pydantic_models import Phone
from models.pydantic_enabled_models import Laptop

app = FastAPI()

items = [
    "Phone",
    "Laptop",
    "Desktop computer",
    "Monitor"
]

phones = [
    Phone(1, "iphone 13", "apple 13 gen iphone", 699, 10),
    Phone(2, "iphone 14", "apple 14 gen iphone", 899, 10),
    Phone(3, "iphone 15", "apple 15 gen iphone", 1099, 5),
    Phone(4, "pixel 9", "Google flagship 9 gen phone", 899, 10)
]

laptops = [
    Laptop(id=1, name="HP Elitebook", desc="Top model from HP for Office", price=999, quantity=4),
    Laptop(id=2, name="Dell Yoga", desc="Top model from Dell for Office", price=1199, quantity=2),
    Laptop(id=3, name="Macbook Pro", desc="Top model from Apple for Office", price=1599, quantity=4)
]

@app.get("/")
def greet():
    return "Welcome to root level"

@app.get("/items")
def get_items():
    return items

@app.get("/phones")
def get_all_phones():
    return phones

@app.get("/phones/{id}")
def get_phone_by_id(id: int):
    for phone in phones:
        if(phone.id == id):
            return phone
    
    return "Phone not found"

@app.get("/laptops")
def get_all_laptops():
    return laptops

@app.get("/laptops/{id}")
def get_laptop_by_id(id: int):
    for laptop in laptops:
        if(laptop.id == id):
            return laptop
    
    return "Laptop not found"

#Post endpoint in FastAPI need Pydantic Basemodels
@app.post("/laptops")
def add_new_phone(laptop: Laptop):
    laptops.append(laptop)
    return "Laptop Successfully added"