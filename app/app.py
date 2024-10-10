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
    return render_template('index.html')

@app.route('/CreateBook', methods=['POST'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
