### 1. Environment Setup

First, ensure you have Python installed on your system. Python 3.6 or later is recommended. You also need pip for installing packages.

#### Installing Flask and SQLite
Open your terminal or command prompt and install Flask:

bash
`pip install Flask`

### 2. Testing the Application

You can test your API endpoints using tools like Postman or cURL.

#### Testing with cURL

- *GET /api/books*

  bash
  curl http://127.0.0.1:5000/api/books
  

- *POST /api/books*

  bash
  curl -X POST -H "Content-Type: application/json" -d '{"title":"New Book", "author":"Author Name", "published_year":2023}' http://127.0.0.1:5000/api/books
  

- *PUT /api/books/{id}*

  bash
  curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Book", "author":"Updated Author", "published_year":2024}' http://127.0.0.1:5000/api/books/1
