from fastapi import FastAPI
import uvicorn
from routers.user import user
from routers.expense import expense
from database.create_tables import create_all_tables

app = FastAPI()
app.include_router(user)
app.include_router(expense)


@app.get("/create_tables")
def create_tables():
    create_all_tables()
    return "Tablas creadas satisfactoriamente"

@app.get("/")
def root():
    return {"message": "Hi from FastAPI"}

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)