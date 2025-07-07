# Django E-commerce Store

A simple, modern e-commerce web application built with Django. This project allows users to browse products, add them to a cart, checkout, and view their order history. User authentication is included for a personalized experience.

---

## Features

- User registration, login, and logout
- Product listing and detail pages
- Add to cart, update quantity, and remove items
- Checkout and order placement
- View order history
- Admin interface for product management
- Media storage with Cloudinary
- Responsive, user-friendly UI

---

## Directory Structure

```
Djago/
├── db.sqlite3
├── ecommerce/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media/
│   └── products/
│       ├── my_photo.jpg
│       ├── sneakers.jpg
│       ├── Tshirt.jpg
│       └── watch.webp
├── Procfile
├── requirements.txt
├── store/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── check_user.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_product_image.py
│   │   └── 0003_order.py
│   ├── models.py
│   ├── templates/
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── detail.html
│   │   ├── index.html
│   │   ├── my_orders.html
│   │   └── registration/
│   │       ├── login.html
│   │       ├── logout.html
│   │       └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── venv/
```

---

## Tech Stack

- **Backend:** Django 5.2.4
- **Database:** SQLite (default), PostgreSQL (production-ready)
- **Media Storage:** Cloudinary
- **Static Files:** WhiteNoise
- **Deployment:** Gunicorn, Procfile (for platforms like Heroku/Render)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Djago
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
   - Visit `http://127.0.0.1:8000/` in your browser.
   - Admin: `http://127.0.0.1:8000/admin/`

---

## Usage

- **Browse Products:**
  - Home page lists all products with images, prices, and details.
- **Product Details:**
  - Click on a product to view its description and add it to your cart.
- **Cart:**
  - View, update, or remove items. Proceed to checkout.
- **Checkout:**
  - Place your order and view a confirmation.
- **Order History:**
  - View your past orders from the 'My Orders' page.
- **Authentication:**
  - Register, login, and logout securely.
- **Admin:**
  - Manage products via the Django admin interface.

---

## Models Overview

- **Product:** name, description, price, image, created_at
- **Order:** user, items (JSON), total, created_at

---

## Deployment

- Uses a `Procfile` for deployment with Gunicorn.
- Cloudinary is configured for media storage (see `ecommerce/settings.py`).
- Static files are served with WhiteNoise.

---

## License

This project is for educational/demo purposes. Please adapt as needed for production use. 
