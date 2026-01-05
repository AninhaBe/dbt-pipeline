import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_weather_data(city: str):
    api_key = os.getenv('OPENWEATHER_API_KEY')

    if not api_key:
        logger.error("Api key não encontrada")
        return None

    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        logger.info(f'Weather data for {city}: {weather_data}')
        return weather_data
    except requests.RequestException as e:
        logger.error(f"erro ao trazer os dados: {e}")

if __name__ == "__main__":
    city = 'São Paulo'
    get_weather_data(city)