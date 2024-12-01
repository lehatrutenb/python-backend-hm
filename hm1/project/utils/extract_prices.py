from models import product

def extract_prices(products: list[product.Product]) -> list[int]:
    return list(map(lambda pr: pr.get_price(), products))
