from celery.app import Celery
from .env import env

rabbitmq_url = env.get("RABBITMQ_URL", "amqp://guest:guest@localhost:5672")

celery_app = Celery(__name__, broker=rabbitmq_url, backend="rpc://")
