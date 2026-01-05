from connect_db import connect_to_database
from extract_api import get_weather_data
import logging
from dotenv import load_dotenv
import psycopg2

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def insert_weather_data(conn, city, weather_data):
    if conn is None:
        logger.error("conexão com database indisponível")
        return None

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO weather_data.city_weather (
                                city,
                                temperature,
                                weather_description,
                                wind_speed,
                                time,
                                insert_at,
                                timezone
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    to_timestamp(%s),
                    NOW(),
                    %s
                    );
            """, (
                weather_data['name'],
                weather_data['main']['temp'],
                weather_data['weather'][0]['description'],
                weather_data['wind']['speed'],
                weather_data['dt'],
                weather_data['timezone']
            ))
            conn.commit()
            logger.info(f"dados para {city} inseridos com sucesso")
    except psycopg2.Error as e:
        logger.error(f'erro ao inserir os dados do tempo')

if __name__ == "__main__":
    city = 'São Paulo'
    weather_data = get_weather_data(city)
    conn = connect_to_database()

    insert_weather_data(conn, city, weather_data)