from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import router  # Import the router
from fastapi.staticfiles import StaticFiles  # Import StaticFiles


# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(router)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="frontend"), name="static")
app.include_router(router)


