from app.models.user import User
from database import db


class UserService:
  def save_change(user: User):
    db.session.add(user)
    db.session.commit()