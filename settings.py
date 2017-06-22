import os

MYSQL_USERNAME = os.getenv("APP_MYSQL_USERNAME", "root")
MYSQL_PASSWORD = os.getenv("APP_MYSQL_PASSWORD", "my-secret-pw")
MYSQL_SCOREBOARD_DB_NAME = os.getenv("APP_MYSQL_SCOREBOARD_DB_NAME", "test")

RETRY_PERIOD = 10  # seconds
RETRY_ATTEMPTS = 10
