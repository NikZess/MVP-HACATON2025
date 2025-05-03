import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    db_url: str = f'sqlite+aiosqlite:///{BASE_DIR}/database.db'
    db_echo: bool = True
    
<<<<<<< HEAD
class AdminData(BaseSettings):
    admin_username: str = os.getenv("ADMIN_USERNAME")
    admin_password: str = os.getenv("ADMIN_PASSWORD")
    
=======
>>>>>>> a661f3b (config file with a env variables)
class JWTData(BaseSettings):
    JWT_secret_key: str = os.getenv("JWT_SECRET_KEY")

class BotToken(BaseSettings):
<<<<<<< HEAD
    bot_token: str = os.getenv("7880169088:AAEC0f_wAV95lE3-axFMmwyQTukdvs9mEO4")

settings = Settings()
admin_data = AdminData()
=======
    bot_token: str = os.getenv("BOT_TOKEN")

settings = Settings()
>>>>>>> a661f3b (config file with a env variables)
JWT_data = JWTData()
bot_data = BotToken()