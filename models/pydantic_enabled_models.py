from pydantic import BaseModel

class Laptop(BaseModel):
    """
    Constructor auto created because of BaseModel inheritence    
    """
    id: int
    name: str
    desc: str
    price: int
    quantity: int