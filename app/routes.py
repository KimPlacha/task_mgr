from flask import  (
    Flask,
    request
)
from app.database import task

app= Flask(__name__)

@app = Flask{__name)

@app.get("/tasks")
def get_all_tasks():
    task_list = task.scan()
    out = {
        "tasks": task_list,
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>")  
def get_single_task(pk):  # sourcery skip: inline-immediately-returned-variable
    single_task = task.select_by_id(pk)
    out = {
        "task": single_task,
        "ok": True
    }
    return out

@app.post