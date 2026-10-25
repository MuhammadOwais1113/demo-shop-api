PRODUCTS = [
    {"id": 1, "name": "Mechanical Keyboard", "price_cents": 8900},
    {"id": 2, "name": "USB-C Hub", "price_cents": 3450},
    {"id": 3, "name": "Desk Mat", "price_cents": 1900},
]


def find_product(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


def cart_total(items):
    total = 0
    for product_id, quantity in items:
        product = find_product(product_id)
        if product is None:
            raise ValueError(f"unknown product {product_id}")
        total += product["price_cents"] * quantity
    return total
