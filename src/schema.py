from pydantic import BaseModel
from datetime import datetime


# =========================
# Base schema (shared fields)
# =========================
class PhoneBase(BaseModel):
    brand: str
    model: str
    year_of_manufacture: int
    cost: int
    sale_cost: int
    discount_percent: int
    type_of_piece: str
    in_stock: bool
    stock_count: int
    rating: float
    warranty_months: int


# =========================
# Create schema (POST)
# =========================
class PhoneCreate(PhoneBase):
    """
    Used when client creates a phone.
    Client DOES NOT send:
    - id
    - created_at
    - last_updated
    """
    pass


# =========================
# Update schema (PUT / PATCH)
# =========================
class PhoneUpdate(PhoneBase):
    """
    Used for updates.
    (Later you can make fields optional for PATCH)
    """
    pass


# =========================
# Response schema (DB → client)
# =========================
class PhoneResponse(PhoneBase):
    id: int
    created_at: datetime
    last_updated: datetime

    class Config:
        from_attributes = True  # REQUIRED for SQLAlchemy
