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
   git clone https://github.com/MatthewGUser/SE_Advanced-API-Development.git
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
   python run.py
   ```

## Usage

- Access the API at `http://localhost:5000`.
- Use the `/login` route to obtain a token for authentication.
- Explore the inventory management routes for CRUD operations.

## Testing

# ! FINISH LATER |

Run the tests using:

```
pytest
```

## License

This project is licensed under the MIT License.

# Checklist for Testing

1. **Rate Limiting and Caching:**

- **Rate Limiting:** Test the rate-limited route to ensure it enforces the rate limit.
  - Endpoint: `/rate_limit/limited-route`
  - Expected behavior: After a certain number of requests (e.g., 5), subsequent requests should return a `429 Too Many Requests` status.
- **Caching:** Test the cached route to ensure it returns cached responses.
  - Endpoint: `/cache/cached-route`
  - Expected behavior: The response should be cached for a specified duration (e.g., 60 seconds).

2. **Token Authentication:**

- **Login:** Test the login route to ensure it returns a token for valid credentials.
  - Endpoint: `/auth/login`
  - Method: `POST`
  - Payload: `{"email": "test@example.com", "password": "password"}`
  - Expected behavior: The response should include a token.
- **Protected Route:** Test a protected route to ensure it requires a valid token.
  - Endpoint: `/service_ticket/my-tickets`
  - Method: `GET`
  - Header: `Authorization: Bearer <token>`
  - Expected behavior: The response should return the user's service tickets if the token is valid.

3. **Advanced Queries:**

- **Update Service Tickets:** Test the route to update service tickets by adding/removing mechanics.
  - Endpoint: `/service_ticket/<ticket_id>/edit`
  - Method: `PUT`
  - Payload: `{"remove_ids": [1, 2], "add_ids": [3, 4]}`
  - Expected behavior: The service ticket should be updated with the specified mechanics.
- **List Mechanics:** Test the route to list mechanics ordered by the number of tickets worked on.
  - Endpoint: `/queries/mechanics`
  - Method: `GET`
  - Expected behavior: The response should list mechanics ordered by the number of tickets worked on.
- **Pagination:** Test the GET Customers route with pagination.
  - Endpoint: `/queries/customers`
  - Method: `GET`
  - Query Params: `?page=1&per_page=10`
  - Expected behavior: The response should return a paginated list of customers.

4. **Inventory Management:**

- **CRUD Operations:** Test the CRUD routes for inventory management.
  - **Create Inventory:**
    - Endpoint: `/inventory/`
    - Method: `POST`
    - Payload: `{"name": "Part A", "price": 100}`
    - Expected behavior: The inventory item should be created.
  - **Get Inventory:**
    - Endpoint: `/inventory/<id>`
    - Method: `GET`
    - Expected behavior: The response should return the inventory item with the specified ID.
  - **Update Inventory:**
    - Endpoint: `/inventory/<id>`
    - Method: `PUT`
    - Payload: `{"name": "Part B", "price": 150}`
    - Expected behavior: The inventory item should be updated.
  - **Delete Inventory:**
    - Endpoint: `/inventory/<id>`
    - Method: `DELETE`
    - Expected behavior: The inventory item should be deleted.
- **Associate Part with Service Ticket:** Test the route to associate a part with a service ticket.
  - Endpoint: `/service_ticket/<ticket_id>/add_part`
  - Method: `POST`
  - Payload: `{"part_id": 1}`
  - Expected behavior: The part should be associated with the service ticket.

5. **General Testing:**

- **Run Unit Tests:** Ensure all unit tests pass.
  - Command: `python -m unittest discover tests`
- **Postman Collection:** Test all routes using Postman and export the collection.
  - Ensure all endpoints are tested and responses are as expected.

## Example Postman Collection

1. **Auth:**

- `POST /auth/login`

2. **Rate Limiting:**

- `GET /rate_limit/limited-route`

3. **Caching:**

- `GET /cache/cached-route`

4. **Service Ticket:**

- `GET /service_ticket/my-tickets`
- `PUT /service_ticket/<ticket_id>/edit`
- `POST /service_ticket/<ticket_id>/add_part`

5. **Inventory:**

- `POST /inventory/`
- `GET /inventory/<id>`
- `PUT /inventory/<id>`
- `DELETE /inventory/<id>`

6. **Queries:**

- `GET /queries/customers`
- `GET /queries/mechanics`

## Summary

- **Rate Limiting and Caching:** Test rate-limited and cached routes.
- **Token Authentication:** Test login and protected routes.
- **Advanced Queries:** Test updating service tickets, listing mechanics, and pagination.
- **Inventory Management:** Test CRUD operations and associating parts with service tickets.
- **General Testing:** Run unit tests and test all routes using Postman.
