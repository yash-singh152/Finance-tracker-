# 💰 Finance Tracker API

A RESTful backend API for tracking personal income and expenses, built with **Django** and **Django REST Framework**.

---

## 🚀 Features

- ✅ Full CRUD for financial transactions
- ✅ Filter by type (`income` / `expense`), category, and date
- ✅ Search by title, description, or category
- ✅ Sort by date or amount
- ✅ Summary endpoint — total income, expense & balance
- ✅ Browsable API via DRF

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Framework | Django 5.x |
| API | Django REST Framework |
| Filtering | django-filter |
| Database | SQLite3 (dev) |

---

## 📁 Project Structure

```
finance(backend)/
├── finance_tracker/          # Django project root
│   ├── finance_tracker/
│   │   ├── settings.py       # Project settings
│   │   ├── urls.py           # Root URL configuration
│   │   └── wsgi.py
│   ├── transactions/         # Transactions app
│   │   ├── models.py         # Transaction model
│   │   ├── serializers.py    # DRF serializer
│   │   ├── views.py          # ViewSet with summary action
│   │   ├── urls.py           # App-level URL router
│   │   └── migrations/
│   ├── db.sqlite3            # SQLite database (local only)
│   └── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yash-singh152/Finance-tracker-.git
cd Finance-tracker-
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
cd finance_tracker
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

The API will be available at **http://127.0.0.1:8000/**

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/transactions/` | List all transactions |
| `POST` | `/transactions/` | Create a new transaction |
| `GET` | `/transactions/{id}/` | Retrieve a transaction |
| `PUT` | `/transactions/{id}/` | Update a transaction |
| `PATCH` | `/transactions/{id}/` | Partially update a transaction |
| `DELETE` | `/transactions/{id}/` | Delete a transaction |
| `GET` | `/transactions/summary/` | Get income/expense totals & balance |

---

## 📦 Transaction Fields

```json
{
  "id": 1,
  "title": "Freelance payment",
  "amount": "5000.00",
  "transaction_type": "income",
  "category": "Freelance",
  "description": "Payment for web project",
  "date": "2026-04-01",
  "created_at": "2026-04-01T10:00:00Z"
}
```

### Field Reference

| Field | Type | Options |
|---|---|---|
| `title` | string | Any text |
| `amount` | decimal | e.g. `999.99` |
| `transaction_type` | string | `income` or `expense` |
| `category` | string | Optional, e.g. `Food`, `Salary` |
| `description` | string | Optional notes |
| `date` | date | `YYYY-MM-DD` |

---

## 🔍 Filtering, Search & Ordering

```
# Filter by type
GET /transactions/?transaction_type=expense

# Filter by category
GET /transactions/?category=Food

# Filter by date
GET /transactions/?date=2026-04-01

# Search
GET /transactions/?search=salary

# Order by amount (descending)
GET /transactions/?ordering=-amount

# Order by date (ascending)
GET /transactions/?ordering=date
```

---

## 📊 Summary Endpoint

```
GET /transactions/summary/
```

Response:
```json
{
  "total_income": 50000.00,
  "total_expense": 12000.00,
  "balance": 38000.00
}
```

---

## 🗄️ Database

This project uses **SQLite3** by default (no setup required). For production, switch to **PostgreSQL** by updating `DATABASES` in `settings.py`.

---

## 📄 License

MIT License — feel free to use and modify.
