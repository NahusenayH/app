from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import auth_controller, post_controller
from app.models.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Post Management API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_controller.router, tags=["Authentication"])
app.include_router(post_controller.router, tags=["Posts"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)