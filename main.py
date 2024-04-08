import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import strawberry
from strawberry.fastapi import GraphQLRouter
from Graphql.query import Query
from Graphql.mutation import Mutation
from config import db
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn.error")
    logger.setLevel(logging.INFO)

class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

def get_graphql_context():
    return {
        "db": db,
        "logger": logging.getLogger("uvicorn.info"),
    }

def init__app():
    setup_logging()
    app = FastAPI()

    @app.on_event("startup")
    async def startup_event():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown_event():
        await db.close()
        
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(CustomException)
    async def custom_exception_handler(request, exc: CustomException):
        return JSONResponse(
            status_code=400,
            content={"message": f"An error occurred: {exc.name}"},
        )

    @app.get('/')
    def home():
        return RedirectResponse(url='/graphql')
    
    @app.get("/health")
    async def health_check():
        return JSONResponse(
            status_code=200,
            content={"status": "healthy"},
        )
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)#, context_getter=get_graphql_context)
    app.include_router(graphql_app, prefix="/graphql")
    return app

app = init__app()

if __name__ == '__main__':
    uvicorn.run( app="main:app", host="localhost", port=8888, reload=True)
