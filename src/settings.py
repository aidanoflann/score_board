import os

MYSQL_USERNAME = os.getenv("APP_MYSQL_USERNAME", "root")
MYSQL_PASSWORD = os.getenv("APP_MYSQL_PASSWORD", "my-secret-pw")
MYSQL_SCOREBOARD_DB_NAME = os.getenv("APP_MYSQL_SCOREBOARD_DB_NAME", "test")
MYSQL_DB_URL = os.getenv("APP_MYSQL_DB_URL", "mysql_db")

STARTUP_WAIT = 20
RETRY_PERIOD = 1  # seconds
RETRY_ATTEMPTS = 3

try:
    from local_settings import *
except ImportError:
    pass
