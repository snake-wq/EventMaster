from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import User, Category, Event


app = FastAPI(
    title="EventMaster API",
    description="Backend приложения EventMaster",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "EventMaster API работает"
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ]


@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()

    return [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description
        }
        for category in categories
    ]


@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()

    return [
        {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "location": event.location,
            "price": float(event.price) if event.price is not None else 0,
            "max_participants": event.max_participants
        }
        for event in events
    ]