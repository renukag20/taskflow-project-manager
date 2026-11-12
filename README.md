# TaskFlow – Django front-end project manager

A basic project management UI built with Django templates, plain CSS and sample data.
No database models are used, so there is nothing to migrate.

## Run it

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Pages

| URL | What it shows |
|---|---|
| `/` | Dashboard with stats, upcoming tasks, active projects |
| `/projects/` | Project cards with progress and team |
| `/projects/<id>/` | Kanban board (To Do / In Progress / Done) |
| `/tasks/` | Task table with status filter tabs |
| `/team/` | Team member cards |

## Where things live

- `core/data.py` – sample projects, tasks and team (edit this to change content)
- `core/views.py` – views that pass the data to templates
- `core/templates/core/` – HTML templates (`base.html` is the shared layout)
- `core/static/core/style.css` – all styling

## Next steps

Replace `core/data.py` with Django models (`Project`, `Task`, `Member`), run
`makemigrations` and `migrate`, and make the "New project" / "New task" buttons
open real forms.
