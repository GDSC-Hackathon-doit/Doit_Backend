from fastapi import FastAPI
import routers as article_router
# from . import models, database
# models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(article_router.router, prefix="/article", tags=["article"])

# To create the initial SQLite database, run the following lines after running the server for the first time:
# from . import models, database
# models.Base.metadata.create_all(bind=database.engine)

