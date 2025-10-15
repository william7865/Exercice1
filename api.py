from flask import Flask, jsonify, request
from todo_cli.repository.json_repository import JSONTaskRepository
from todo_cli.models.task import Task, Priority

app = Flask(__name__)
repo = JSONTaskRepository()


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Lister toutes les tâches"""
    tasks = [t.to_dict() for t in repo.all()]
    return jsonify(tasks), 200


@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    """Afficher une tâche spécifique"""
    task = repo.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200


@app.route("/tasks", methods=["POST"])
def add_task():
    """Créer une nouvelle tâche"""
    data = request.get_json(force=True)
    if not data or "title" not in data:
        return jsonify({"error": "Missing field: title"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        priority=Priority(data.get("priority", "medium")),
        due_date=None,
    )
    repo.save(task)
    return jsonify(task.to_dict()), 201


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """Modifier une tâche existante"""
    task = repo.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(force=True)
    if "title" in data:
        task.title = data["title"]
    if "description" in data:
        task.description = data["description"]
    if "priority" in data:
        task.priority = Priority(data["priority"])
    task.touch()
    repo.save(task)

    return jsonify(task.to_dict()), 200


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Supprimer une tâche"""
    deleted = repo.delete(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted"}), 200


@app.route("/tasks/<task_id>/done", methods=["PATCH"])
def mark_done(task_id):
    """Marquer une tâche comme terminée"""
    task = repo.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    task.mark_done()
    repo.save(task)
    return jsonify(task.to_dict()), 200


if __name__ == "__main__":
    app.run(debug=True)