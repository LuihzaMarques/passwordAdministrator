from fastapi import FastAPI
from routes.user import user


app = FastAPI(
    docs_url="/password",
    title="Password API in Python",
    description="API para geração de senhas",
    version="1.0",
)

app.include_router(user)