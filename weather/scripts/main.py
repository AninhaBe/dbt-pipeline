import logging
import os
from dotenv import load_dotenv

from connect_db import connect_to_database
from create_schema import create_schema_and_table
from extract_api import get_weather_data
from insert_data import insert_weather_data

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def run_pipeline(city: str) -> None:
    logger.info("iniciando pipeline de weather...")

    weather_data = get_weather_data(city)
    if not weather_data:
        logger.error("falha ao extrair dados da API. encerrando pipeline")
        return None

    conn = connect_to_database()
    if conn is None:
        logger.error("falha ao conectar no Postgres. encerrando pipeline")
        return None

    try:
        with conn:
            create_schema_and_table(conn)
            insert_weather_data(conn, city, weather_data)

        logger.info("pipeline finalizada com sucesso")
    except Exception as e:
        logger.exception(f"pipeline falhou com erro inesperado: {e}")
    finally:
        try:
            conn.close()
            logger.info("conexão com Postgres fechada")
        except Exception:
            pass


if __name__ == "__main__":
    city = "Curitiba"
    run_pipeline(city)
