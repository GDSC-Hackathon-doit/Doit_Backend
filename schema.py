from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ArticleBase(BaseModel):
    title: str
    subTitle: str
    description: str
    hardness: int
    source: str
    sourceUrl: str
    imgUrl: str
    imgAlt: str
    publishedTime: datetime
    click: Optional[int] = None
    like: Optional[int] = None

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
