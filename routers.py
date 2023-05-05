from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import schema, database, crud
from models import Article

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.Article)
def create_article(article: schema.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db, article)

@router.get("/", response_model=List[schema.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_articles(db, skip=skip, limit=limit)

@router.get("/{article_id}", response_model=schema.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.put("/{article_id}", response_model=schema.Article)
def update_article(article_id: int, article: schema.ArticleCreate, db: Session = Depends(get_db)):
    db_article = crud.update_article(db, article_id, article)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article

@router.delete("/{article_id}", response_model=schema.Article)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article
