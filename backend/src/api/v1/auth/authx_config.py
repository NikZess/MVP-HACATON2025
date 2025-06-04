import os
from dotenv import load_dotenv, find_dotenv

from authx import AuthX, AuthXConfig
from ...core.config import JWT_data

load_dotenv(find_dotenv())

config = AuthXConfig()
config.JWT_SECRET_KEY = JWT_data.JWT_secret_key
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]
config.JWT_COOKIE_CSRF_PROTECT = False

security = AuthX(config=config)