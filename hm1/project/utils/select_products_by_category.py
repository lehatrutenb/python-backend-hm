from models import product

def select_products_by_category(products: list[product.Product], category: str) -> list[product.Product]:
     return list(filter(lambda product: product.category==category, products)) # get_category()?
