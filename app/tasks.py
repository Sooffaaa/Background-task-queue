import time
import random
from .worker import celery_app

@celery_app.task(
		bind=True,
		autoretry_for=(Exception,),
		retry_kwargs={'max_retries': 3, 'countdown': 5}
)
def send_notification_task(self, message: str, email: str):
		print(f"--- [Worker] Начал обрабатывать уведомление для {email} ---")

		time.sleep(5)

		if random.random() < 0.3:
				print(f"!!! [Worker] Ошибка сети при отправке на {email} !!!")
				raise Exception("Connection Error")

		print(f"--- [Worker] Успешно отправлено: '{message}' на почту {email} ---")
		return {"status": "success", "to": email}


