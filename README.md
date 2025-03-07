the# 🚀 Flask-based Expense Tracker

A simple yet powerful **Expense Tracker API** built with **Flask & SQLAlchemy**.
This API helps users manage **expense categories** and **track their spending** efficiently.

---

## 📌 Features

- Manage Categories & Expenses (CRUD operations)
- SQLite Database with SQLAlchemy ORM
- Automatic Database Migrations using Alembic
- Cascade Deletes (Deleting a category removes related expenses)
- UUID-based Identification for secure and unique records
- Foreign Key Constraint Handling in SQLite
- Database migrations with Alembic.
- Fully backend-based

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Obcodelab/expense-tracker.git
cd expense-tracker
```

### 2️⃣ Create & Activate a Virtual Environment

```bash
# On Linux or Macos
python3 -m venv venv
source venv/bin/activate
```

```bash
# On Windows
python -m venv venv

# For cmd and powershell
venv\Scripts\activate

# For git bash
source venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup the Database

Run Alembic migrations to create the required database tables:

```bash
flask db upgrade
```

### 5️⃣ Start the Flask Server

```bash
flask run --reload
```

📌 API Endpoints

The API will be available at http://127.0.0.1:5000

🔹 Categories
| Method | Endpoint | Description |
| :------: | :------: | :------: |
| POST | /categories | Create a new category |
| GET | /categories | Get all categories |
| GET | /categories/`<uuid>` | Get a category |
| PUT | /categories/`<uuid>` | Update a category |
| DELETE | /categories/`<uuid>` | Delete a category & related expenses|
| DELETE | /categories | Delete all category & related expenses|

🔹 Expenses
| Method | Endpoint | Description |
| :------: | :------: | :------: |
| POST | /expenses | Create a new expense |
| GET | /expenses | Get all expenses |
| GET | /expenses/`<uuid>` | Get an expense |
| PUT | /expenses/`<uuid>` | Update an expense |
| DELETE | /expenses/`<uuid>` | Delete an expense |
| DELETE | /expenses/`<uuid>` | Delete all expenses |

## 🏗 Tech Stack

- Flask (Backend)
- SQLite (Database)
- SQLAlchemy & Alembic (ORM & Migrations)

## 🤝 Contributing

- Fork the repository
- Create a new branch (git checkout -b feature-name)
- Commit your changes (git commit -m "Added new feature")
- Push to the branch (git push origin feature-name)
- Open a Pull Request 🎉

## 📜 License

This project is open-source under the MIT License.
