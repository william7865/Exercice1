# ToDoList CLI + API REST (MVC + POO + Flask)

Une mini application **ToDoList** en **Python**, avec :
- Une **interface en ligne de commande (CLI)**  
- Une **API REST Flask** pour accéder aux tâches via HTTP  
- Une architecture claire **MVC**  
- Une structure orientée **POO** (Programmation Orientée Objet)

---

## 🚀 Fonctionnalités principales
- Ajouter, afficher, modifier, supprimer des tâches  
- Marquer une tâche comme terminée  
- Lister les tâches avec filtres et tris  
- Sauvegarde locale au format JSON (`~/.todo_cli/tasks.json`)  
- **API REST Flask** exposant les mêmes opérations  
- Architecture **MVC** et **Repository Pattern**  
- Typage Python, dataclasses, et tests unitaires  

---

## 📁 Structure du projet

```
Exercice1-Nom-Prenom/
├── app.py                 # CLI (interface en ligne de commande)
├── api.py                 # 🌐 API REST Flask
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
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient :
```
flask
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

## 🌐 API REST Flask

### ▶️ Lancer l’API
```bash
python api.py
```

L’API sera disponible sur :
> http://127.0.0.1:5000

Si le port 5000 est déjà utilisé :
```bash
python api.py --port 5050
```

ou modifie la ligne :
```python
app.run(debug=True, port=5050)
```

---

### 📡 Endpoints disponibles

| Méthode | Route | Description |
|----------|--------|-------------|
| `GET` | `/` | Page d’accueil de l’API |
| `GET` | `/tasks` | Lister les tâches |
| `POST` | `/tasks` | Créer une tâche |
| `GET` | `/tasks/<id>` | Afficher une tâche |
| `PUT` | `/tasks/<id>` | Modifier une tâche |
| `PATCH` | `/tasks/<id>/done` | Marquer terminée |
| `DELETE` | `/tasks/<id>` | Supprimer une tâche |

---

#### 📋 Lister toutes les tâches
```bash
curl http://127.0.0.1:5000/tasks
```

#### ✅ Marquer une tâche comme terminée
```bash
curl -X PATCH http://127.0.0.1:5000/tasks/<ID_TACHE>/done
```

#### 🗑️ Supprimer une tâche
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/<ID_TACHE>
```

---

## 🧠 Concepts appliqués
- **POO** : `Task`, `RecurringTask`, `Priority`, `Status`  
- **MVC** :  
  - `models` → logique métier  
  - `controllers` → gestion CLI  
  - `views` → affichage console  
  - `repository` → persistance JSON  
- **Flask REST API** : accès HTTP aux mêmes fonctionnalités  
- **Tests unitaires** avec `unittest`  

---

## 🧪 Lancer les tests
```bash
python -m unittest
```