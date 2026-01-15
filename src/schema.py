from pydantic import BaseModel

class Phone_schema(BaseModel):
    id: int
    brand: str
    model: str
    type_of_piece: str
    year_of_manufacture: int
    sale_cost: float
    rating: float
    discount_percent: float
    in_stock: bool
    warranty_years: int
    created_at: str
    last_updated: str

