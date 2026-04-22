from fastapi import Depends, FastAPI
from models.non_pydantic_models import Phone
from models.pydantic_enabled_models import Laptop
from models import database_models
from database_config import session, engine
from sqlalchemy.orm import Session

app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

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

def get_db_connection():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Init method needs its own session   
    """
    db = session()
    count = db.query(database_models.LaptopEntity).count()
    if count == 0:
        for laptop in laptops:
            db.add(database_models.LaptopEntity(**laptop.model_dump()))
        db.commit()
    db.close()

init_db()

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
def get_all_laptops(db: Session= Depends(get_db_connection)):
    return db.query(database_models.LaptopEntity).all()

@app.get("/laptops/{id}")
def get_laptop_by_id(id: int, db: Session= Depends(get_db_connection)):
    laptop = db.query(database_models.LaptopEntity).filter(database_models.LaptopEntity.id == id).first()
    if laptop:
        return laptop
    return "Laptop not found"

#Post endpoint in FastAPI need Pydantic Basemodels
@app.post("/laptops")
def add_new_laptop(laptop: Laptop, db: Session= Depends(get_db_connection)):
    db.add(database_models.LaptopEntity(**laptop.model_dump()))
    db.commit()
    return "Laptop Successfully added"

@app.put("/laptops/{id}")
def update_laptop(id: int, laptop: Laptop, db: Session= Depends(get_db_connection)):
    db_laptop = db.query(database_models.LaptopEntity).filter(database_models.LaptopEntity.id == id).first()
    if db_laptop:
        db_laptop.name = laptop.name
        db_laptop.desc = laptop.desc
        db_laptop.price = laptop.price
        db_laptop.quantity = laptop.quantity
        db.commit()
        return "Laptop updated"
    
    return "Laptop not found!"

@app.delete("/laptops/{id}")
def delete_laptop(id: int, db: Session= Depends(get_db_connection)):
    db_laptop = db.query(database_models.LaptopEntity).filter(database_models.LaptopEntity.id == id).first()
    if db_laptop:
        db.delete(db_laptop)
        db.commit()
        return "Laptop Deleted"
    
    return "Laptop not found!"