import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/database.db'
    db_echo: bool = True
    
    
class JWTData(BaseSettings):
    JWT_secret_key: str = os.getenv("JWT_SECRET_KEY")

class BotToken(BaseSettings):
    bot_token: str = os.getenv("BOT_TOKEN")

settings = Settings()
JWT_data = JWTData()
bot_data = BotToken()