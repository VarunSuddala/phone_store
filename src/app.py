import fastapi
from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
import data

data_values=data.data
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello ! welcome": "countinue shopping !"}
#filters
@app.get("/phones/")
def filter_phone(
    min_price:int=Query(0),
    max_price:int=Query(10**6),
    brand:str=None,
    model:str=None,
    type:str=None,
    year:int=None,
    in_stock:bool=None
):
    result=[]

    for p in data_values:
        if not (min_price <= p["sale_cost"] <= max_price):
            continue
        if brand and p["brand"].lower() != brand.lower():
            continue
        if model and p["model"].lower() != model.lower():
            continue
        if type and p["type_of_piece"].lower() != type.lower():
            continue
        if year and p["year_of_manufacture"] != year:
            continue
        if in_stock is not None and p["in_stock"] != in_stock:
            continue

        result.append(p)
    if result : 
        return {
            "count" : len(result),
            "phones":result
        }
    else: raise HTTPException(status_code=404,detail="not found")
#sorting 
@app.get("/phone/sort")
def phones_sort(
    rate:bool =False,
    discount:bool=False,
    price:bool=False

):
    
    if sum(rate,discount,price)>1:
        raise HTTPException(status_code=400,detail="choose only one sorting parameter")
    if rate :
        phones=sorted(data_values,key=lambda x: x["rating"] ,reverse=True)
    if discount:
        phones=sorted(data_values,key=lambda x:x["discount_percent"],reverse=True)
    if price:
        phones=sorted(data_values,key=lambda x:x["sale_cost"])
    return {
        "count":len(phones),
        "phones":phones
    }

    


