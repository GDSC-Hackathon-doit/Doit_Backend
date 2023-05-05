from sqlalchemy.orm import Session
import models, schema

def create_article(db: Session, article: schema.ArticleCreate):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def update_article(db: Session, article_id: int, article: schema.ArticleCreate):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if db_article is None:
        return None

    article_data = article.dict()
    for key, value in article_data.items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if db_article is None:
        return None

    db.delete(db_article)
    db.commit()
    return db_article
