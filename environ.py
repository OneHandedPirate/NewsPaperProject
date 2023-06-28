from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_USE_TLS = bool(os.getenv('EMAIL_USE_TLS'))
EMAIL_USE_SSL = bool(os.getenv('EMAIL_USE_SSL'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


DJANGO_SK = os.getenv('DJANGO_SK')
