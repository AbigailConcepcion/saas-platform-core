from fastapi import FastAPI
from pymongo import MongoClient
import redis

app = FastAPI()

mongo = MongoClient("mongodb://mongodb:27017")
db = mongo["analytics"]

cache = redis.Redis(host="redis", port=6379)

@app.get("/v1/analytics/total-orders")
def total_orders():
    cached = cache.get("total_orders")
    if cached:
        return {"total_orders": int(cached)}

    total = db.orders.count_documents({})
    cache.set("total_orders", total, ex=60)
    return {"total_orders": total}
