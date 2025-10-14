# Exercice1-Nom-Prenom — ToDoList CLI (MVC + POO)

Une mini API en ligne de commande pour gérer une liste de tâches en Python, avec une structure type MVC,
POO, et bonnes pratiques (types, docstrings, logging, tests). Aucune dépendance externe.

## Installation
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .  # optionnel, usage direct possible
```

## Utilisation rapide
```bash
python app.py add "Finir le rapport" -d "Chapitre 3" -p high --due 2025-10-31
python app.py list
python app.py done <ID_TACHE>
python app.py show <ID_TACHE>
python app.py edit <ID_TACHE> --title "Nouveau titre"
python app.py delete <ID_TACHE>
```

Le stockage est effectué dans `~/.todo_cli/tasks.json` par défaut (modifiable via variable d'env `TODO_CLI_DB`).

## Structure
```
Exercice1-Nom-Prenom/
├── app.py                 # Point d'entrée CLI (contrôleur)
├── todo_cli/
│   ├── controllers/
│   │   └── todo_controller.py
│   ├── models/
│   │   ├── task.py
│   │   └── storage.py
│   ├── repository/
│   │   └── json_repository.py
│   └── views/
│       └── cli_view.py
└── tests/
    └── test_core.py
```

## Tests
```bash
python -m unittest
```

## Nom du dépôt GitHub
Créez un dépôt **public** nommé : `Exercice1-Nom-Prenom` et poussez-y ce contenu.
