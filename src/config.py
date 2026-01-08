"""
Configuration module to load environment variables
"""
import os
from pathlib import Path
from typing import Optional

# Try to load python-dotenv if available
try:
    from dotenv import load_dotenv
    # Load .env file from project root
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    print("python-dotenv not installed. Using system environment variables only.")
    print("Install with: pip install python-dotenv")


class Config:
    """Application configuration loaded from environment variables"""
    
    # MLflow & DagsHub Configuration
    MLFLOW_TRACKING_URI: str = os.getenv(
        'MLFLOW_TRACKING_URI',
        'https://dagshub.com/AshutoshMishra-UJ/Delivery_Time-Prediction.mlflow'
    )
    DAGSHUB_USER_NAME: str = os.getenv('DAGSHUB_USER_NAME', 'AshutoshMishra-UJ')
    DAGSHUB_REPO_NAME: str = os.getenv('DAGSHUB_REPO_NAME', 'Delivery_Time-Prediction')
    DAGSHUB_TOKEN: Optional[str] = os.getenv('DAGSHUB_TOKEN')
    
    # MLflow Credentials
    MLFLOW_TRACKING_USERNAME: str = os.getenv('MLFLOW_TRACKING_USERNAME', DAGSHUB_USER_NAME)
    MLFLOW_TRACKING_PASSWORD: Optional[str] = os.getenv('MLFLOW_TRACKING_PASSWORD', DAGSHUB_TOKEN)
    
    # Model Configuration
    MODEL_NAME: str = os.getenv('MODEL_NAME', 'delivery_time_prediction_model')
    MODEL_STAGE: str = os.getenv('MODEL_STAGE', 'Production')
    
    # API Configuration
    API_HOST: str = os.getenv('API_HOST', '0.0.0.0')
    API_PORT: int = int(os.getenv('API_PORT', '8000'))
    API_RELOAD: bool = os.getenv('API_RELOAD', 'False').lower() == 'true'
    
    # Application Settings
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def display_config(cls):
        """Display current configuration (without sensitive data)"""
        print("=" * 50)
        print("Application Configuration")
        print("=" * 50)
        print(f"Environment: {cls.ENVIRONMENT}")
        print(f"Debug Mode: {cls.DEBUG}")
        print(f"MLflow Tracking URI: {cls.MLFLOW_TRACKING_URI}")
        print(f"DagsHub User: {cls.DAGSHUB_USER_NAME}")
        print(f"DagsHub Repo: {cls.DAGSHUB_REPO_NAME}")
        print(f"Model Name: {cls.MODEL_NAME}")
        print(f"Model Stage: {cls.MODEL_STAGE}")
        print(f"API Host: {cls.API_HOST}:{cls.API_PORT}")
        print(f"Log Level: {cls.LOG_LEVEL}")
        print("=" * 50)


# Create a singleton instance
config = Config()

if __name__ == "__main__":
    # Display configuration when run directly
    Config.display_config()
