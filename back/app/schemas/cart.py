from pydantic import BaseModel, Field

class CartItemBase(BaseModel):
    product_id: int = Field(description='Product ID')
    quantity: int = Field(gt=0, description='Quantity must be positive')


class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(description='Product ID')
    quantity: int = Field(gt=0, description='New quantity must be positive')


class CartItem(BaseModel):
    id: int
    name: str
    price: float
    quantity: int = Field(description='Quantity in cart')
    subtotal: float = Field(description='Total price for this item(price * quantity)')
    image_url: str | None = Field(description='Product image URL')

class CartResponse(BaseModel):
    items: list[CartItem] = Field(description='List of items in cart')
    total: float = Field(description='Total cart price')
    items_count: int = Field(description='Total number of items in cart')