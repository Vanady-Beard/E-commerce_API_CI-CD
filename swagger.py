from flasgger import Swagger

def configure_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }

    swagger_template = {
        "info": {
            "title": "E-commerce API",
            "description": """
                This API allows you to manage an e-commerce application. You can:
                - Add and view products
                - View and manage orders
                - Add and view users
                Each section below provides detailed information about the API endpoints, including what parameters to pass and what responses to expect.
            """,
            "version": "1.0.0",
            "contact": {
                "name": "Your Name",
                "url": "https://yourwebsite.com",
                "email": "your_email@example.com",
            },
        },
        "host": "localhost:5000",
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ],
        "tags": [
            {
                "name": "Users",
                "description": "Operations related to user management"
            },
            {
                "name": "Products",
                "description": "Operations related to product management"
            },
            {
                "name": "Orders",
                "description": "Operations related to order management"
            }
        ],
    }

    Swagger(app, config=swagger_config, template=swagger_template)
