class Phone:
    id: int
    name: str
    desc: str
    price: int
    quantity: int

    def __init__(self, id: int, name: str, desc: str, price: int, quantity: int):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity