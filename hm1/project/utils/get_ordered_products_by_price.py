from models import product

def get_ordered_products_by_price(products: list[product.Product]) -> list[product.Product]:
    return sorted(products, key=lambda product: -product.get_price())
