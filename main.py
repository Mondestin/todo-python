from fastapi import FastAPI
# Documentation
from documentations.description import app_description
from documentations.tags import tags_metadata

#Routers
import routers.router_todos
import routers.router_auth

# API Initilization
app = FastAPI(
    title="Todo API",
    description=app_description,
    openapi_tags= tags_metadata,
    docs_url='/docs'
)
# Define app routes
app.include_router(routers.router_todos.router)
app.include_router(routers.router_auth.router)


