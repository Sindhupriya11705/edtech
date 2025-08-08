from fastapi import FastAPI
from .routers import auth,users,courses,recommendations
app=FastAPI( title="EdTech Adaptive Learning Platform API",
    version="1.0.0",
    description="Backend service for personalized learning paths, assessments, and feedback.")
app.include_router(auth.router,prefix="/api/v1/auth",tags=["Auth"])
app.include_router(users.router,prefix="/api/v1/users",tags=["Users"])
app.include_router(courses.router,prefix="/api/v1/courses",tags=["Courses"])
app.include_router(recommendations.router,
                   prefix="/api/v1/recommendations", tags=["Recommendations"])
@app.get("/")
async def root():
    return {"message":"Welcome to EdTech Adaptive Learning Platform API"}