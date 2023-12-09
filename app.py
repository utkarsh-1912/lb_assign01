from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/books', methods=['GET'])
def get_all_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in books])  # Convert rows to dict

@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)',
                 (new_book['title'], new_book['author'], new_book['published_year']))
    conn.commit()
    conn.close()
    return jsonify(new_book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    update_details = request.json
    conn = get_db_connection()
    conn.execute('UPDATE books SET title = ?, author = ?, published_year = ? WHERE id = ?',
                 (update_details['title'], update_details['author'], update_details['published_year'], book_id))
    conn.commit()
    conn.close()
    return jsonify(update_details)

if __name__ == '__main__':
    app.run(debug=True)
