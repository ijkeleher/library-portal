from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='db',
        user='root',
        password='password',
        database='booksdb'
    )
    return connection

@app.route('/', methods=['GET'])
def index():
    connection = get_db_connection()
    books = []
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, title, author, loan_status, borrower FROM Books")
        books = cursor.fetchall()  # Fetch all rows from the Books table
        cursor.close()
    return render_template('index.html', books=books)

@app.route('/createBook', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Books (title, author) VALUES (%s, %s)", (title, author))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('index'))

@app.route('/checkout', methods=['POST'])
def checkout_book():
    book_id = request.form['book_id']
    user_id = request.form['user_id']
    
    # Check if the book exists and is available
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT loan_status FROM Books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if book and book[0] == 'Available':
        # Check if the user exists
        cursor.execute("SELECT * FROM Users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if user:
            # Update book to be on loan and assign borrower
            cursor.execute("""
                UPDATE Books
                SET loan_status = 'On Loan', borrower = %s
                WHERE id = %s
            """, (user_id, book_id))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('index'))
        else:
            return 'User does not exist', 400
    else:
        return 'Book not available or does not exist', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
