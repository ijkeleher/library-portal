# Library Portal

Simple Flask app with a MySQL database. This application is intended to serve as a Library Management System (LMS) for a local community library.

This repo includes:

1. A **Flask app** that serves the library backend.
2. A **MySQL database** for storing Books, Loans, Users etc.
3. An **HTML form** served at `localhost:8000` that lets you perform operations like adding new books to the database.

### Instructions

1. **Build and run the services:**

```bash
docker-compose up --build
```

2. **Access the app** by visiting `http://localhost:8000`.

3. **Add a book** via the form on the page. The book details will be inserted into the MySQL `Books` table.

This setup uses `docker-compose` to spin up the MySQL container and the Flask app. The `db/init.sql` script automatically sets up the `Books` table inside the MySQL container when it's first started.