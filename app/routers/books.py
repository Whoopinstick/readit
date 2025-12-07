from fastapi import APIRouter, HTTPException, status, Path

router = APIRouter(prefix="/books", tags=["books"])

books_db = {1: {"name": "Book1", "description": "The first Book", "year": 2025}}

@router.get("/")
async def get_all_books():
    return {"response": books_db}


@router.get("/{book_id}")
async def get_book_by_id(book_id: int = Path(gt=0)):
    try:
        return {"response": books_db[book_id]}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book ID {book_id} not found")

