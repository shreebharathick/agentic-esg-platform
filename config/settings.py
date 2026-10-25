import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Agentic ESG Platform"
    VERSION: str = "1.0.0"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ERP_API_BASE_URL: str = os.getenv("ERP_API_BASE_URL", "")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()