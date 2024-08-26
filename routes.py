from flask import Blueprint, jsonify, request
from models import User, Product, Order, OrderItem, db

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    """
    Get a list of all users
    ---
    tags:
      - Users
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
              created_at:
                type: string
                format: date-time
    """
    users = User.query.all()
    users_data = [{"id": u.id, "username": u.username, "email": u.email, "created_at": u.created_at} for u in users]
    return jsonify(users_data)

@api.route('/products', methods=['POST'])
def add_product():
    """
    Add a new product
    ---
    tags:
      - Products
    parameters:
      - in: body
        name: product
        description: The product to create
        schema:
          type: object
          required:
            - name
            - price
          properties:
            name:
              type: string
            description:
              type: string
            price:
              type: number
              format: float
    responses:
      201:
        description: Product added successfully
    """
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

@api.route('/products', methods=['GET'])
def get_products():
    """
    Get a list of all products
    ---
    tags:
      - Products
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              description:
                type: string
              price:
                type: number
                format: float
              created_at:
                type: string
                format: date-time
    """
    products = Product.query.all()
    products_data = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "created_at": p.created_at} for p in products]
    return jsonify(products_data)

@api.route('/orders', methods=['GET'])
def get_orders():
    """
    Get a list of all orders
    ---
    tags:
      - Orders
    responses:
      200:
        description: A list of orders
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              user_id:
                type: integer
              total:
                type: number
                format: float
              created_at:
                type: string
                format: date-time
    """
    orders = Order.query.all()
    orders_data = [{"id": o.id, "user_id": o.user_id, "total": o.total, "created_at": o.created_at} for o in orders]
    return jsonify(orders_data)



