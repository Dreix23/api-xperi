from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import redis

app = FastAPI()

# Define tu modelo Pydantic como antes
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Configura el cliente de Redis para conectar con tu instancia de Redis
redis_client = redis.Redis(
    host='witty-thrush-36026.upstash.io',
    port=36026,
    password='8a94ddc1266b4e29b89765d780f215cf',
    ssl=True,
    ssl_cert_reqs=None
)

@app.post("/items/")
def create_item(item: Item):
    # Convierte el ítem (que es una instancia de Pydantic) en un diccionario
    # y luego en una cadena JSON para almacenarlo en Redis
    item_json = item.json()
    redis_client.set(item.name, item_json)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    # Obtiene todos los ítems almacenados en Redis
    items = []
    for key in redis_client.scan_iter("*"):
        item_json = redis_client.get(key)
        items.append(Item.parse_raw(item_json))
    return items
