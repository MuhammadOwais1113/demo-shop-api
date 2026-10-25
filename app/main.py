from flask import Flask, jsonify, request

from app import config
from app.models import PRODUCTS, cart_total, find_product

app = Flask(__name__)
app.config["DATA_DIR"] = config.DATA_DIR


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/products")
def list_products():
    return jsonify(PRODUCTS)


@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = find_product(product_id)
    if product is None:
        return jsonify(error="not found"), 404
    return jsonify(product)


@app.route("/cart/total", methods=["POST"])
def total():
    payload = request.get_json(silent=True) or {}
    items = [(i["id"], i["quantity"]) for i in payload.get("items", [])]
    try:
        return jsonify(total_cents=cart_total(items), currency=config.CURRENCY)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
