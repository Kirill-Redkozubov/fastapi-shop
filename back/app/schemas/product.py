from pydantic import BaseModel, Field
from datetime import datetime
from .category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(min_length=5, max_length=200, description='Product name')
    description: str | None = Field(None, description='Product description')
    price: float = Field(gt=0, description='Product price(must be positive)')
    category_id: int = Field(description='Category id')
    image_url: str | None = Field(description='Product image URL')

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(description='Unique product ID')
    name: str
    description: str | None
    price: float
    category_id: int
    image_url: str | None
    created_at: datetime
    category: CategoryResponse = Field(description='Product category details')

    class Config:
        form_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(description='Total number of products')

