from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
from src.data import data
from src.schema import Phone_schema
from datetime import datetime

data_values=data
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
    
    if sum([rate,discount,price])>1:
        raise HTTPException(status_code=400,detail="choose only one sorting parameter")
    if rate :
        phones=sorted(data_values,key=lambda x: x["rating"] ,reverse=True)
    if discount:
        phones=sorted(data_values,key=lambda x:x["discount_percent"],reverse=True)
    if price:
        phones=sorted(data_values,key=lambda x:x["sale_cost"])

    if not(rate,discount,price):
        raise HTTPException(status_code=400 , detail="Choose rate, discount or price ")
    return {
        "count":len(phones),
        "phones":phones
    }

@app.post("/phones/admin/add")
def add_phone(phone:Phone_schema):
    new_phone=phone.dict()
    new_phone["id"]=max(p["id"] for p in data_values)+1
    new_phone["created_at"]=datetime.now().strftime("%Y-%m-%d %H:%M")
    new_phone["last_updated"]=new_phone["created_at"]
    data_values.append(new_phone)

    return {
        "message":"phone added successfully",
        "phone":new_phone
    }

@app.put("/phone/admin/update")
def update_phone(id:int,product:Phone_schema):
    for i in range(len(data_values)):
        if data_values[i]["id"]==id:
            data_values[i].update(product.dict())
            data_values[i]["last_updated"]=datetime.now().strftime("%y-%m-%d %H:%M")
            return{"message":f"{id} is updated"}
    raise HTTPException(status_code=404,detail="not found")

@app.delete("/phone/admin/delete")
def del_phone (id:int):
    for i,j in enumerate(data_values):
        if j["id"]==id:
            deleted=data_values.pop(i)
            return{"message":f"{id} is deleted","deleted":deleted}
    raise HTTPException(status_code=404,detail="not found")


