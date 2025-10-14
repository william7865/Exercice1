import unittest
from todo_cli.models.task import Task, Priority, Status
from todo_cli.repository.json_repository import JSONTaskRepository
from tempfile import NamedTemporaryFile
from datetime import date


class TestCore(unittest.TestCase):
    def test_create_and_get(self):
        with NamedTemporaryFile(suffix=".json") as f:
            repo = JSONTaskRepository(db_path=f.name)
            t = Task(title="Test", description="desc", priority=Priority.high)
            repo.save(t)
            got = repo.get(t.id)
            self.assertIsNotNone(got)
            self.assertEqual(got.title, "Test")

    def test_mark_done(self):
        with NamedTemporaryFile(suffix=".json") as f:
            repo = JSONTaskRepository(db_path=f.name)
            t = Task(title="Test")
            repo.save(t)
            t.mark_done()
            repo.save(t)
            self.assertEqual(repo.get(t.id).status, Status.done)

    def test_due_date_sort(self):
        with NamedTemporaryFile(suffix=".json") as f:
            repo = JSONTaskRepository(db_path=f.name)
            t1 = Task(title="A", due_date=date(2025, 1, 1))
            t2 = Task(title="B", due_date=None)
            repo.save(t1); repo.save(t2)
            tasks = list(repo.all())
            tasks.sort(key=lambda t: (t.due_date is None, t.due_date))
            self.assertEqual(tasks[0].title, "A")


if __name__ == "__main__":
    unittest.main()
