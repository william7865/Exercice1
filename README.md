# Exercice1-Nom-Prenom — ToDoList CLI (MVC + POO)

Une mini API en ligne de commande pour gérer une liste de tâches en **Python**, suivant une architecture **MVC** et utilisant la **programmation orientée objet (POO)**.

---

## 🚀 Fonctionnalités principales
- Ajouter, afficher, modifier, supprimer des tâches  
- Marquer une tâche comme terminée  
- Lister les tâches (avec filtres et tris)  
- Stockage local JSON (`~/.todo_cli/tasks.json`)  
- CLI ergonomique avec `argparse`  
- Code organisé selon le modèle MVC  
- Typage, dataclasses, et tests unitaires  

---

## 📁 Structure du projet

```
Exercice1-Nom-Prenom/
├── app.py                 # Point d’entrée CLI
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

---

## ⚙️ Installation (macOS / Linux)

```bash
unzip Exercice1-Nom-Prenom.zip
cd Exercice1-Nom-Prenom
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## 🧑‍💻 Utilisation de la CLI

### ➕ Ajouter une tâche
```bash
python app.py add "Finir le rapport" -d "Chapitre 3 à compléter" -p high --due 2025-10-31
```

### 📋 Lister toutes les tâches
```bash
python app.py list
python app.py list --status pending
python app.py list --sort priority
```

### 🔍 Afficher une tâche spécifique
```bash
python app.py show <ID_TACHE>
```

### ✏️ Modifier une tâche
```bash
python app.py edit <ID_TACHE> --title "Nouveau titre" --priority low
```

### ✅ Marquer une tâche comme terminée
```bash
python app.py done <ID_TACHE>
```

### 🗑️ Supprimer une tâche
```bash
python app.py delete <ID_TACHE>
```

---

## 🧠 Concepts appliqués
- **POO** : `Task`, `RecurringTask`, `Priority`, `Status`  
- **MVC** :  
  - `models` → logique métier  
  - `controllers` → gestion des commandes  
  - `views` → affichage CLI  
- **Repository pattern** pour la persistance (`JSONTaskRepository`)  
- **Tests unitaires** avec `unittest`  

---

## 🧪 Lancer les tests
```bash
python -m unittest
```

---

## 🗂️ Persistance
Les tâches sont sauvegardées dans un fichier JSON :
```
~/.todo_cli/tasks.json
```