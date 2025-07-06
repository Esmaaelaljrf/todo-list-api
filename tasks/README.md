# To-Do List API with Authentication

A Django REST API project that allows users to manage their personal to-do tasks securely.

## Features

- User registration and login with JWT authentication
- CRUD operations for tasks (Create, Read, Update, Delete)
- Tasks linked to individual users
- Email uniqueness validation and password encryption
- Pagination and filtering for task list

## Technology Stack

- Python
- Django & Django REST Framework
- SQLite (development database)
- djangorestframework-simplejwt for JWT authentication

## Project Structure

- `config/` - Django project settings and configurations
- `tasks/` - Django app containing models, serializers, views, and URLs for tasks
- `users/` (optional) - For user-related functionality (if separated)

## How to Run

1. Create and activate virtual environment
2. Install dependencies (`pip install -r requirements.txt`)
3. Run migrations (`python manage.py migrate`)
4. Start the server (`python manage.py runserver`)

## Next Steps

- Complete user registration and login endpoints
- Implement authentication and permissions on task views
- Add pagination and filtering to task list
- Write unit tests
- Prepare project for deployment

