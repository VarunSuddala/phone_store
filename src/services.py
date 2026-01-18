
from src.data import data
from datetime import datetime
data_values=data


def filter_phone(
    min_price:int=0,
    max_price:int=10**6,
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
    if not result:
        return None
    return result

def phones_sort(sort_by:str):
    phones=[]
    if sort_by == "rate":
        phones=sorted(data_values,key=lambda x: x["rating"] ,reverse=True)
    elif sort_by == "discount":
        phones=sorted(data_values,key=lambda x:x["discount_percent"],reverse=True)
    elif sort_by == "price":
        phones=sorted(data_values,key=lambda x:x["sale_cost"])
    return phones
#==========================================================================================================================
def add_phone(phone:dict):
    for p in data_values:
        if p["model"].lower() == phone["model"].lower() and  p["year_of_manufacture"] == phone["year_of_manufacture"]:
            return None
    new_phone = {
        "id": max(p["id"] for p in data_values) + 1,
        "brand": phone["brand"],
        "model": phone["model"],
        "year_of_manufacture": phone["year_of_manufacture"],
        "cost": phone["cost"],
        "sale_cost": phone["sale_cost"],
        "discount_percent": phone["discount_percent"],
        "type_of_piece": phone["type_of_piece"],
        "in_stock": phone["in_stock"],
        "stock_count": phone["stock_count"],
        "rating": phone["rating"],
        "warranty_months": phone["warranty_months"],
        "created_at": datetime.now(),
        "last_updated": datetime.now()
    }
    data_values.append(new_phone)
    return new_phone
#==========================================================================================================================
def update_phone(id:int,product:dict):
    for i ,j in enumerate(data_values):
        if j["id"]==id:
            j.update(product)
            j["last_updated"]=datetime.now()
            return j 
    return None
#==========================================================================================================================
def del_phone (id:int):
    for i,j in enumerate(data_values):
        if j["id"]==id:
            if j["stock_count"]!=0:
                return None
            del data_values[i]
            return j
    return None