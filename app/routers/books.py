from fastapi import APIRouter, HTTPException, status, Path
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter(prefix="/books", tags=["books"])

books_db = {1: {"name": "Book1", "description": "The first Book", "year": 2025}}


class CreateBookModel(BaseModel):
    name: str = Field(min_length=1, max_length=500)
    description: str = Field(min_length=3, max_length=1_000)
    year: int = Field(gt=0, lte=datetime.now().year)


class ResponseBookModel(CreateBookModel):
    id: int


@router.get("/")
async def get_all_books():
    return {"response": books_db}


@router.get("/{book_id}")
async def get_book_by_id(book_id: int = Path(gt=0)):
    try:
        return {"response": books_db[book_id]}
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Book ID {book_id} not found"
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)


@router.post("/")
async def create_book(book: CreateBookModel):
    book_id = max(books_db) + 1
    books_db[book_id] = {
        "name": book.name,
        "description": book.description,
        "year": book.year,
    }
    print(books_db)
    return {"response": books_db[book_id]}
