from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    item: List[str]
    quantity: Dict[str,int]

class BlogPost(BaseModel):
    title: str
    content: str
    img_url: Optional[str] = None

cartData = {
    "user_id":1,
    "item":["Laptop", "KeyBoard", "Mouse"],
    "quantity": {"Laptop": 1, "Keyboard": 1, "Mouse": 1}
}

cart = Cart(**cartData)
print(cart)