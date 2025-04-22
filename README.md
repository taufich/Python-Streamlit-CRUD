# 🗂️ Streamlit + PostgreSQL CRUD App

This project is a lightweight web application built using **Streamlit** that connects to a **PostgreSQL** database to perform basic **CRUD operations** (Create, Read, Update, Delete) on a simple `app_users` table.

Ideal for small admin panels, educational purposes, and internal data management tools.

---

## 🚀 Features

- 🔄 Full CRUD functionality:
  - **Create**: Add new users with name and email
  - **Read**: View all records in a table
  - **Update**: Modify existing records by ID
  - **Delete**: Remove records by ID
- 📦 Integrated PostgreSQL backend
- 🖥️ Intuitive web interface built with Streamlit

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — Python-based web UI
- [PostgreSQL](https://www.postgresql.org/) — Relational database
- [psycopg2](https://www.psycopg.org/) — PostgreSQL adapter for Python

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/streamlit-postgres-crud.git
   cd streamlit-postgres-crud
   ```

2. **Create and activate a virtual environment (optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL**
   - Ensure PostgreSQL is running.
   - Create a database named `python_crud`.
   - Create a table `app_users` with the following schema:
     ```sql
     CREATE TABLE app_users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(255),
       email VARCHAR(255)
     );
     ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

---

## 🔐 Database Credentials

Currently, database connection settings are hardcoded:

```python
host="localhost"
user="postgres"
password="admin"
database="python_crud"
```

> 🔒 **Security Tip**: In production, move these to environment variables or use a `.env` file.

---

## 🧠 Notes

- Make sure the `app_users` table exists before using the app.
- The database must be accessible from the environment where the app runs.

---

## 📃 License

MIT License. Feel free to use, share, and improve.

---

## 🙋‍♂️ Contributions

Pull requests and suggestions are welcome!
