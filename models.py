from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    subTitle = Column(String, index=True, nullable=True)
    hardness = Column(Integer, nullable=False)
    source = Column(String, nullable=True)
    sourceUrl = Column(String, nullable=False)
    imgAlt = Column(String, nullable=True)
    imgUrl = Column(String, nullable=False)
    description = Column(String, nullable=True)
    publishedTime = Column(DateTime, nullable=False)
    click = Column(Integer, nullable=True, default=None)
    like = Column(Integer, nullable=True, default=None)


    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', subTitle='{self.subTitle}, hardness={self.hardness}, sourceUrl='{self.sourceUrl}', source='{self.source}', img_alt='{self.img_alt}', img_url='{self.img_url}', description='{self.description}', original_date={self.original_date}, click={self.click}, like={self.like})>"
