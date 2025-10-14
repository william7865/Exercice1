from __future__ import annotations
from typing import Iterable
from ..models.task import Task
from datetime import datetime


def print_task(task: Task) -> None:
    due = task.due_date.isoformat() if task.due_date else "-"
    print(f"[{task.id}] {task.title} (prio={task.priority}, status={task.status}, due={due})")
    if task.description:
        print(f"    {task.description}")


def print_list(tasks: Iterable[Task]) -> None:
    tasks = list(tasks)
    if not tasks:
        print("Aucune tâche.")
        return
    for t in tasks:
        print_task(t)


def print_success(message: str) -> None:
    print(f"✔ {message}")


def print_error(message: str) -> None:
    print(f"✖ {message}")
