from django.http import Http404
from django.shortcuts import render

from . import data


def dashboard(request):
    tasks = [data.enrich_task(t) for t in data.TASKS]
    stats = {
        "projects": len(data.PROJECTS),
        "active": len([p for p in data.PROJECTS if p["status"] == "In Progress"]),
        "tasks": len(tasks),
        "done": len([t for t in tasks if t["status"] == "Done"]),
        "team": len(data.TEAM),
    }
    upcoming = [t for t in tasks if t["status"] != "Done"][:6]
    projects = [data.enrich_project(p) for p in data.PROJECTS if p["status"] != "Completed"]
    return render(request, "core/dashboard.html", {
        "page": "dashboard",
        "stats": stats,
        "upcoming": upcoming,
        "projects": projects,
    })


def project_list(request):
    projects = [data.enrich_project(p) for p in data.PROJECTS]
    return render(request, "core/projects.html", {"page": "projects", "projects": projects})


def project_detail(request, project_id):
    proj = data.project(project_id)
    if proj is None:
        raise Http404("Project not found")
    tasks = [data.enrich_task(t) for t in data.TASKS if t["project"] == project_id]
    columns = [
        {"name": s, "tasks": [t for t in tasks if t["status"] == s]}
        for s in data.STATUSES
    ]
    return render(request, "core/project_detail.html", {
        "page": "projects",
        "project": data.enrich_project(proj),
        "columns": columns,
    })


def task_list(request):
    tasks = [data.enrich_task(t) for t in data.TASKS]
    status = request.GET.get("status", "")
    if status in data.STATUSES:
        tasks = [t for t in tasks if t["status"] == status]
    return render(request, "core/tasks.html", {
        "page": "tasks",
        "tasks": tasks,
        "statuses": data.STATUSES,
        "active_status": status,
    })


def team(request):
    members = []
    for m in data.TEAM:
        mm = dict(m)
        mm["task_count"] = len([t for t in data.TASKS if t["assignee"] == m["id"] and t["status"] != "Done"])
        mm["project_count"] = len([p for p in data.PROJECTS if m["id"] in p["members"]])
        members.append(mm)
    return render(request, "core/team.html", {"page": "team", "members": members})
