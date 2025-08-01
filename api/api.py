from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.todos_route import todo_api_router

app = FastAPI(
    title="Python FastApi and MongoDB at Atlas",
    description="01-08-2025 - FastAPI serving CRUD towards MongoDB Atlas",
    version="0.0.1",
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
        
        },
        
        )

origins = [
    "https://fastapi-mongo-crud.vercel.app",
    "http://localhost",
    "http://localhost:8080",
    "0.0.0.0/0",
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(todo_api_router)
