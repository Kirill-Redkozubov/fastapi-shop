from sqlalchemy.orm import Session
from typing import List

from ..repositories.product_repository import ProductRepository
from ..schemas.product import ProductResponse, ProductCreate, ProductListResponse
from fastapi import HTTPException, status


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)

    def get_all_products(self) -> ProductListResponse:
        products = self.product_repository.get_all()
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response, total=len(products_response))

    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f'category with product_id: {product_id} not found')
        return ProductResponse.model_validate(product)

    def get_product_by_category(self, category_id: int) -> ProductListResponse:
        products = self.product_repository.get_by_category(category_id)
        if not products:
            raise HTTPException(status_code=404, detail=f'Category: {category_id} not found')
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(products=products_response, total=len(products_response))

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        product = self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)