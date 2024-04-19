from tortoise.contrib.pydantic import pydantic_model_creator

from src.db.models import Users

UserInSchema = pydantic_model_creator(
    Users, name="userIn", exclude_readonly=True
)

UserOutSchema = pydantic_model_creator(
    Users, name="UserOUt", exclude=['password', 'created_at', 'modified_at']
)

UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=['created_at', 'modified_at']
)