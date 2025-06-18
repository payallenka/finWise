# Finance AI Backend

This is the Django backend for the Finance AI application. It provides RESTful APIs for managing financial transactions, budgets, and market data.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register a new user
- `GET /api/users/me/` - Get current user details
- `PUT /api/users/me/` - Update user details

### Transactions
- `GET /api/transactions/` - List all transactions
- `POST /api/transactions/` - Create a new transaction
- `GET /api/transactions/{id}/` - Get transaction details
- `PUT /api/transactions/{id}/` - Update transaction
- `DELETE /api/transactions/{id}/` - Delete transaction
- `GET /api/transactions/summary/` - Get transaction summary

### Budget Categories
- `GET /api/budget-categories/` - List all budget categories
- `POST /api/budget-categories/` - Create a new budget category
- `GET /api/budget-categories/{id}/` - Get budget category details
- `PUT /api/budget-categories/{id}/` - Update budget category
- `DELETE /api/budget-categories/{id}/` - Delete budget category

### Market Data
- `GET /api/market-data/` - Get latest market data
- `POST /api/market-data/` - Create new market data entry

## Development

The backend uses Django REST Framework for API development. Key features include:

- Custom user model with financial information
- Session-based authentication
- CORS support for frontend integration
- Comprehensive API endpoints for all features
- Admin interface for data management

## Frontend Integration

The backend is configured to work with the React frontend running on `http://localhost:3000`. CORS is enabled for this origin. 