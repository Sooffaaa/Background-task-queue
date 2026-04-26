import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
		"tasks",
		broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
		backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
)

celery_app.autodiscover_tasks(['app'])

celery_app.conf.worker_prefetch_multiplier = 1
celery_app.conf.task_acks_late = True

