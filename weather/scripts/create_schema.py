from connect_db import connect_to_database
import logging
from dotenv import load_dotenv
import psycopg2

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_schema_and_table(conn):
    if conn is None:
        logger.error("nenhuma conexão disponível")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("CREATE SCHEMA IF NOT EXISTS weather_data;")
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS weather_data.city_weather (
                           id SERIAL PRIMARY KEY,
                           city TEXT,
                           temperature FLOAT,
                           weather_description TEXT,
                           wind_speed FLOAT,
                           time TIMESTAMP,
                           insert_at TIMESTAMP DEFAULT NOW(),
                           timezone TEXT
                        );
            """)
            conn.commit()
            logger.info("schema e tabela criados com sucesso!")
    except psycopg2.Error as e:
        logger.error(f'falha na criação do schema e tabela: {e}')
        return None

if __name__ == "__main__":
    conn = connect_to_database()
    create_schema_and_table(conn)