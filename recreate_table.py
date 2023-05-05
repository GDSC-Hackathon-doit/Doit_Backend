from models import Article
from database import engine

Article.__table__.drop(engine)
Article.__table__.create(engine)
