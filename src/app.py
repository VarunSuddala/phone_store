from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
import src.services as services
from src.schema import PhoneBase, PhoneResponse,PhoneCreate,PhoneUpdate
from datetime import datetime


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello ! welcome": "countinue shopping !"}
#filters
@app.get("/phones/",response_model=list[PhoneResponse])
def phones_filter(
    min_price:int=Query(0),
    max_price:int=Query(10**6),
    brand:str=None,
    model:str=None,
    type:str=None,
    year:int=None,
    in_stock:bool=None
):
    phones=services.filter_phone(
        min_price=min_price,
        max_price=max_price,
        brand=brand,
        model=model,
        type=type,
        year=year,
        in_stock=in_stock
    )
    if not phones:
        raise HTTPException(status_code=404,detail="not found")
    return phones

#sorting 
@app.get("/phone/sort")
def sort(sort_by:str):
    sorted_phones= services.phones_sort(sort_by)
    if not sorted_phones:
        raise HTTPException(status_code=404,detail="not found or invalid sort parameter")
    return sorted_phones

#admin operations
@app.post("/phones/admin/add",response_model=PhoneResponse)
def add_phone(phone:PhoneCreate):
    new_phone= services.add_phone(phone.dict())
    if not new_phone:
        raise HTTPException(status_code=400,detail="phone already exists")
    return new_phone

@app.put("/phone/admin/update",response_model=PhoneResponse)
def update_phone(id:int,product:PhoneUpdate):
    updated_phone= services.update_phone(id,product.dict())
    if not updated_phone:
        raise HTTPException(status_code=404,detail="not found")
    return updated_phone

@app.delete("/phone/admin/delete", response_model=PhoneResponse)
def del_phone(id: int):
    deleted = services.del_phone(id)
    if not deleted:
        raise HTTPException(status_code=400, detail="cannot delete phone with stock count greater than 0 or not found")
    return deleted




print("APP LOADED AS:", __name__)