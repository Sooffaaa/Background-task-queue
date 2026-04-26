from fastapi import FastAPI
from .tasks import send_notification_task

app = FastAPI(title="Background Worker")

@app.get("/")
def read_root():
		return {"message": "complete!"}

@app.post("/notify")
async def notify_user(email: str, text:str):
		task = send_notification_task.delay(text, email)

		return {
        "status": "Task sent to background",
        "task_id": task.id,
        "note": "Пока повар работает, вы можете делать другие запросы!"
    }
