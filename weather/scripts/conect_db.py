import os
import logging
from dotenv import load_dotenv
import psycopg2

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def connect_to_database():
    logger.info("conectando ao banco postgres...")
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("POSTGRES_DB"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD"),
            host = os.getenv("POSTGRES_HOST"),
            port = os.getenv("POSTGRES_PORT"),
        )
        logger.info("conexão realizada com sucesso ao postgresdb")
        return conn
    except psycopg2.Error as e:
        logger.error(f"falha na conexão {e}")
        return None


if __name__ == "__main__":
    connect_to_database()