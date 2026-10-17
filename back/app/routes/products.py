from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.product_service import  ProductService
from ..schemas.product import ProductResponse

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)

@router.get('', response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_all_products()

@router.get('/{product_id}', response_model=ProductResponse)
def get_category(product_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_product_by_id(product_id)

@router.get('/{category_id}', response_model=ProductResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    product_service = ProductService(db)
    return product_service.get_product_by_category(category_id)
