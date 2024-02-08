from app import app
from app.app_config import AppConfig

if __name__ == "__main__":
    app.run(
        port=AppConfig.PORT,
        host=AppConfig.HOST,
        debug=AppConfig.DEBUG
    )  # type: ignore
