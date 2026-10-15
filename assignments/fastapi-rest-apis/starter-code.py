from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find and return the book with this ID, or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=201)
def create_book(book_input: BookInput):
    # TODO: Assign a unique ID, add the new book to books, and return it.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the book with this ID, or raise HTTPException with status 404.
    pass
