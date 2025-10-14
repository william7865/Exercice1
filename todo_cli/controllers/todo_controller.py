from __future__ import annotations
import argparse
from datetime import date
from typing import Optional
from ..repository.json_repository import JSONTaskRepository
from ..models.task import Task, Priority
from ..views.cli_view import print_list, print_task, print_success, print_error


def parse_date(s: Optional[str]) -> Optional[date]:
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        raise argparse.ArgumentTypeError("Format de date attendu: YYYY-MM-DD")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="todo",
        description="ToDoList CLI — MVC + POO (aucune dépendance)",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # add
    sp = sub.add_parser("add", help="Ajouter une tâche")
    sp.add_argument("title", help="Titre")
    sp.add_argument("-d", "--description", default="", help="Description")
    sp.add_argument("-p", "--priority", choices=[e.value for e in Priority], default="medium")
    sp.add_argument("--due", type=parse_date, help="Échéance (YYYY-MM-DD)")

    # list
    sp = sub.add_parser("list", help="Lister les tâches")
    sp.add_argument("--status", choices=["pending", "done", "archived"], help="Filtre statut")
    sp.add_argument("--sort", choices=["created", "due", "priority"], default="created")

    # show
    sp = sub.add_parser("show", help="Afficher une tâche")
    sp.add_argument("id")

    # edit
    sp = sub.add_parser("edit", help="Modifier une tâche")
    sp.add_argument("id")
    sp.add_argument("--title")
    sp.add_argument("--description")
    sp.add_argument("--priority", choices=[e.value for e in Priority])
    sp.add_argument("--due", type=parse_date)

    # done
    sp = sub.add_parser("done", help="Marquer terminée")
    sp.add_argument("id")

    # delete
    sp = sub.add_parser("delete", help="Supprimer une tâche")
    sp.add_argument("id")

    return p


def main(argv: Optional[list[str]] = None) -> None:
    args = build_parser().parse_args(argv)
    repo = JSONTaskRepository()

    if args.cmd == "add":
        task = Task(
            title=args.title,
            description=args.description,
            priority=Priority(args.priority),
            due_date=args.due,
        )
        repo.save(task)
        print_success(f"Tâche créée: {task.id}")
        print_task(task)
        return

    if args.cmd == "list":
        tasks = list(repo.all())
        # filter
        if args.status:
            tasks = [t for t in tasks if t.status.value == args.status]
        # sort
        if args.sort == "created":
            tasks.sort(key=lambda t: t.created_at)
        elif args.sort == "due":
            tasks.sort(key=lambda t: (t.due_date is None, t.due_date))
        elif args.sort == "priority":
            prio_order = {"high": 0, "medium": 1, "low": 2}
            tasks.sort(key=lambda t: prio_order[t.priority.value])
        print_list(tasks)
        return

    if args.cmd == "show":
        task = repo.get(args.id)
        if not task:
            print_error("Tâche introuvable.")
            return
        print_task(task)
        return

    if args.cmd == "edit":
        task = repo.get(args.id)
        if not task:
            print_error("Tâche introuvable.")
            return
        if args.title is not None:
            task.title = args.title
        if args.description is not None:
            task.description = args.description
        if args.priority is not None:
            task.priority = Priority(args.priority)
        if args.due is not None:
            task.due_date = args.due
        task.touch()
        repo.save(task)
        print_success("Tâche mise à jour.")
        print_task(task)
        return

    if args.cmd == "done":
        task = repo.get(args.id)
        if not task:
            print_error("Tâche introuvable.")
            return
        task.mark_done()
        repo.save(task)
        print_success("Tâche terminée.")
        print_task(task)
        return

    if args.cmd == "delete":
        ok = repo.delete(args.id)
        if ok:
            print_success("Tâche supprimée.")
        else:
            print_error("Tâche introuvable.")
        return
