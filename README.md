# Flask API Project

This project is a Flask-based API that includes features such as rate limiting, caching, token authentication, advanced queries, and inventory management.

## Features

- **Rate Limiting**: Implemented using Flask-Limiter to control the number of requests a user can make to the API.
- **Caching**: Utilizes Flask-Caching to improve performance by storing frequently accessed data.
- **Token Authentication**: JWT-based authentication for secure access to protected routes.
- **Advanced Queries**: Supports complex queries for retrieving and updating data.
- **Inventory Management**: CRUD operations for managing inventory items.

## Project Structure

```
flask-api-project
├── instance
├── migrations
├── server
│   ├── blueprints
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── tokens.py
│   │   ├── cache
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── inventory
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── mechanic
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── queries
│   │   │   ├── __init__.py
│   │   │   └── advanced_queries.py
│   │   ├── rate_limiting
│   │   │   ├── __init__.py
│   │   │   └── rate_limit.py
│   │   ├── service_ticket
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── customer.py
│   │   ├── inventory.py
│   │   ├── mechanic.py
│   │   ├── service_ticket.py
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_cache.py
│   ├── test_inventory.py
│   ├── test_queries.py
│   ├── test_rate_limiting.py
│   ├── test_service_ticket.py
├── .env
├── .gitignore
├── advanced-api-development.postman_collection.json
├── README.md
├── requirements.txt
└── run.py
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/MatthewGUser/SE_Advanced-API-Development.git
   cd SE_Advanced-API-Development
   ```
2. Create a virtual environment:

```
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```
venv\Scripts\activate
```

- On macOS/Linux:

```
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Set up environment variables in `.env`.
6. Initialize the database:

```
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

7. Run the application (choose one):

- Using Python directly:

```
python run.py
```

- Using Flask CLI:

```
flask run
```

8. Test API using Postman collection provided in root directory.

- Be sure to create a customer before logging in.

## License

This project is licensed under the MIT License.
