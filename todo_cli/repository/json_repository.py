from __future__ import annotations
from typing import Iterable, Optional, List
from pathlib import Path
import json
from datetime import datetime
from ..models.task import Task
from ..models.storage import TaskRepository
import os


DEFAULT_DB = os.environ.get("TODO_CLI_DB", str(Path.home() / ".todo_cli" / "tasks.json"))


class JSONTaskRepository(TaskRepository):
    """Implémentation simple en JSON local."""

    def __init__(self, db_path: str = DEFAULT_DB) -> None:
        self.path = Path(db_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write([])

    # --- Utils ---
    def _read(self) -> List[dict]:
        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _write(self, items: List[dict]) -> None:
        tmp = self.path.with_suffix(".tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        tmp.replace(self.path)

    # --- Repository API ---
    def all(self) -> Iterable[Task]:
        return [Task.from_dict(d) for d in self._read()]

    def get(self, task_id: str) -> Optional[Task]:
        for d in self._read():
            if d.get("id") == task_id:
                return Task.from_dict(d)
        return None

    def save(self, task: Task) -> None:
        items = self._read()
        for i, d in enumerate(items):
            if d.get("id") == task.id:
                items[i] = task.to_dict()
                self._write(items)
                return
        items.append(task.to_dict())
        self._write(items)

    def delete(self, task_id: str) -> bool:
        items = self._read()
        new_items = [d for d in items if d.get("id") != task_id]
        if len(new_items) != len(items):
            self._write(new_items)
            return True
        return False
