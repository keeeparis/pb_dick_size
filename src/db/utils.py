import datetime
from peewee import *

from src.db.database import User, Interaction

def create_user(id: int, username: str, first_name: str, last_name: str) -> None:
  User.create(id=id, username=username, first_name=first_name, last_name=last_name, created_at=datetime.datetime.now())

def create_interaction(user_id: int, result: int) -> None:
  user = User.get(User.id == user_id)
  Interaction.create(user=user, dick_size_result=result, created_at=datetime.datetime.now())

def user_exists(user_id: int) -> bool:
  try:
    User.get_by_id(user_id)
    return True
  except DoesNotExist:
    return False
  
  
  