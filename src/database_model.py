from sqlalchemy.ext.declartive import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base=declarative_base()
class PhoneBase(Base):
    brand = Column(String)
    model = Column(String)
    year_of_manufacture = Column(Integer)
    cost = Column(Integer)
    sale_cost = Column(Integer)
    discount_percent = Column(Integer)
    type_of_piece = Column(String)
    in_stock = Column(Boolean)
    stock_count = Column(Integer)
    rating = Column(Float)
    warranty_months = Column(Integer)

