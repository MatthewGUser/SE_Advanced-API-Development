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
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── tokens.py
│   ├── cache
│   │   ├── __init__.py
│   │   └── cache.py
│   ├── inventory
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── queries
│   │   ├── __init__.py
│   │   └── advanced_queries.py
│   ├── rate_limiting
│   │   ├── __init__.py
│   │   └── rate_limit.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_cache.py
│   ├── test_inventory.py
│   ├── test_queries.py
│   └── test_rate_limiting.py
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-api-project
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

5. Set up environment variables in the `.env` file.

6. Run the application:
   ```
   flask run
   ```

## Usage

- Access the API at `http://localhost:5000`.
- Use the `/login` route to obtain a token for authentication.
- Explore the inventory management routes for CRUD operations.

## Testing

Run the tests using:
```
pytest
```

## License

This project is licensed under the MIT License.