from fastapi import FastAPI
import uvicorn
from routers import debt_collector, expense, user, debt, installment, auth
from database.create_tables import create_all_tables

app = FastAPI(
    title="Expense Manager",
    description="This is an API for manage my expense, debts, installments and more about finances.",
    version="1.0.0",
    docs_url="/docs",
)
routers_list = [debt_collector, expense, user, debt, installment, auth]
for router in routers_list:
    app.include_router(router)


@app.get("/create_tables")
def create_tables():
    create_all_tables()
    return "Tablas creadas satisfactoriamente"


@app.get("/")
def root():
    return {"message": "Hi, this is my Expense Manager API"}


if __name__ == "__main__":
    uvicorn.run("main:app --reload", port=8000, reload=True)
