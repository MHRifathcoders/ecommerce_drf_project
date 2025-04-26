# 🛒 Multi-Tenant E-commerce API with Role-Based Access Control (Django DRF)

This project is a **Django REST Framework** based backend for a multi-tenant e-commerce platform.  
It features **Admin**, **Vendor**, and **Customer** roles, **JWT authentication**, **Role-Based Access Control (RBAC)**, **caching**, **rate-limiting**, and **Swagger UI** for easy API testing.

---

## 📚 Features

- ✅ Multi-Tenant Architecture (Vendors manage their own products & orders)
- ✅ Role-Based Access Control (Admin, Vendor, Customer)
- ✅ JWT Authentication (Login/Register)
- ✅ CRUD for Products
- ✅ Order Placement and Management
- ✅ Django Signals for Order Notifications
- ✅ Redis Caching (optional for performance)
- ✅ Throttling & Rate Limiting
- ✅ Search, Filter, and Pagination for Products
- ✅ Swagger and ReDoc Auto Documentation

---

## 🚀 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. Create and Activate a Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver


