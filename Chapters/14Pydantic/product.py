from pydantic import BaseModel



class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool



product = {"id":23, "name":"Mercedes", "price":2.3, "in_stock":True}
product = Product(**product)
print(product)