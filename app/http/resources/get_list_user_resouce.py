from typing import List
from app.models.user import User

def format_list_user_response(users: List[User]):
  return [{"id": user.id, "full_name": user.full_name, "email": user.email, "username": user.username} for user in users]
