# 📘 Intro_to_DB

A simple and practical introduction to **databases** using **MySQL** and **Python**.  
This project demonstrates how to design a basic bookstore schema, execute SQL tasks, and connect to a MySQL server through Python.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Setup & Usage](#setup--usage)
- [Task Breakdown](#task-breakdown)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)

---

## 🧩 Overview

The **Intro_to_DB** project walks through essential database operations:
- Creating and managing a **bookstore database**.
- Writing and organizing multiple **SQL task scripts**.
- Using **Python (MySQL Connector)** to interact with MySQL databases.
- Following best practices in version control with `.gitignore`.

This project is part of foundational learning for SQL and Python database handling.

---

## 📁 Repository Structure

| File | Description |
|------|--------------|
| `.gitignore` | Excludes `venv/`, `__pycache__/`, and other local build artifacts. |
| `MySQLServer.py` | Python script that configures and tests a MySQL connection. |
| `alx_book_store.sql` | Creates the initial bookstore schema (database setup). |
| `task_2.sql` | Fixes capitalization of table names. |
| `task_3.sql` | Adds `USE alx_book_store` to ensure correct database context. |
| `task_4.sql` | Displays full description of the `Books` table using `information_schema`. |
| `task_5.sql` | Fixes errors from earlier tasks. |
| `task_6.sql` | Inserts multiple rows into the `Customers` table. |
| `README.md` | Documentation for this repository. |

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:

- **MySQL Server** (latest stable version)
- **Python 3.x**
- **MySQL Connector for Python**

Install the MySQL connector:

```bash
pip install mysql-connector-python
