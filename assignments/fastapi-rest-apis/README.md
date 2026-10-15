# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage a book catalog. Practice defining HTTP endpoints, validating request data, and returning useful status codes.

## 📝 Tasks

### 🛠️ Read Books from the API

#### Description
Complete the read endpoints in `starter-code.py`. The API should let a client retrieve every book or look up one book by its ID.

Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then start the app with `uvicorn starter-code:app --reload`. Open `http://127.0.0.1:8000/docs` to try your endpoints.

#### Requirements
Completed program should:

- Return the full book list from `GET /books`
- Return one matching book from `GET /books/{book_id}`
- Return an HTTP 404 response when the requested book ID does not exist

### 🛠️ Add and Remove Books

#### Description
Complete the create and delete endpoints. Use the provided Pydantic model to validate new book data, and make sure clients receive an appropriate response when a book is added or an ID cannot be found.

#### Requirements
Completed program should:

- Accept a JSON object with `title` and `author` at `POST /books` and assign the new book a unique ID
- Return HTTP 201 when a book is created
- Remove the matching book from `DELETE /books/{book_id}`
- Return HTTP 404 when a delete targets an unknown ID
