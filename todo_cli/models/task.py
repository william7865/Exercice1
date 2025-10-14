from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional, Dict, Any
from datetime import datetime, date
import uuid


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Status(str, Enum):
    pending = "pending"
    done = "done"
    archived = "archived"


@dataclass
class Task:
    """Représente une tâche unique."""

    title: str
    description: str = ""
    priority: Priority = Priority.medium
    due_date: Optional[date] = None
    status: Status = Status.pending
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        """Sérialiser en dict JSON-friendly."""
        d = asdict(self)
        d["priority"] = self.priority.value
        d["status"] = self.status.value
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["due_date"] = self.due_date.isoformat() if self.due_date else None
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Désérialiser depuis un dict."""
        return cls(
            id=data.get("id", uuid.uuid4().hex),
            title=data["title"],
            description=data.get("description", ""),
            priority=Priority(data.get("priority", "medium")),
            due_date=date.fromisoformat(data["due_date"]) if data.get("due_date") else None,
            status=Status(data.get("status", "pending")),
            created_at=datetime.fromisoformat(data["created_at"])
            if data.get("created_at")
            else datetime.utcnow(),
            updated_at=datetime.fromisoformat(data["updated_at"])
            if data.get("updated_at")
            else datetime.utcnow(),
        )

    def mark_done(self) -> None:
        self.status = Status.done
        self.touch()

    def archive(self) -> None:
        self.status = Status.archived
        self.touch()

    def touch(self) -> None:
        self.updated_at = datetime.utcnow()


@dataclass
class RecurringTask(Task):
    """Exemple d'héritage: une tâche récurrente (non exploitée en CLI mais fournie pour la POO)."""
    frequency_days: int = 7
