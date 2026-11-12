"""Sample data for the front-end-only project manager.

Everything lives in memory here, so no database or migrations are needed.
Swap these lists for Django models later when you want real persistence.
"""

TEAM = [
    {"id": 1, "name": "Aarav Sharma", "role": "Project Manager", "initials": "AS", "color": "#6366f1"},
    {"id": 2, "name": "Priya Patil", "role": "Frontend Developer", "initials": "PP", "color": "#ec4899"},
    {"id": 3, "name": "Rohan Deshmukh", "role": "Backend Developer", "initials": "RD", "color": "#14b8a6"},
    {"id": 4, "name": "Sneha Kulkarni", "role": "UI/UX Designer", "initials": "SK", "color": "#f59e0b"},
    {"id": 5, "name": "Vikram Joshi", "role": "QA Engineer", "initials": "VJ", "color": "#8b5cf6"},
]

PROJECTS = [
    {
        "id": 1,
        "name": "Website Redesign",
        "description": "Refresh the company website with a modern look, faster load times and better mobile support.",
        "status": "In Progress",
        "progress": 65,
        "due": "30 Nov 2026",
        "members": [1, 2, 4],
    },
    {
        "id": 2,
        "name": "Mobile App v2",
        "description": "Second major release of the customer mobile app with offline mode and push notifications.",
        "status": "In Progress",
        "progress": 40,
        "due": "20 Dec 2026",
        "members": [1, 2, 3, 5],
    },
    {
        "id": 3,
        "name": "Internal CRM",
        "description": "Build a lightweight CRM for the sales team to track leads and follow-ups.",
        "status": "Planning",
        "progress": 10,
        "due": "28 Feb 2027",
        "members": [1, 3],
    },
    {
        "id": 4,
        "name": "Brand Guidelines",
        "description": "Document logo usage, colours, typography and tone of voice for all teams.",
        "status": "Completed",
        "progress": 100,
        "due": "15 Oct 2026",
        "members": [4, 1],
    },
]

TASKS = [
    {"id": 1, "project": 1, "title": "Create wireframes for home page", "status": "Done", "priority": "High", "assignee": 4, "due": "05 Nov"},
    {"id": 2, "project": 1, "title": "Build responsive navbar", "status": "Done", "priority": "Medium", "assignee": 2, "due": "08 Nov"},
    {"id": 3, "project": 1, "title": "Implement hero section", "status": "In Progress", "priority": "High", "assignee": 2, "due": "14 Nov"},
    {"id": 4, "project": 1, "title": "Optimise images", "status": "To Do", "priority": "Low", "assignee": 2, "due": "20 Nov"},
    {"id": 5, "project": 1, "title": "Cross-browser testing", "status": "To Do", "priority": "Medium", "assignee": 5, "due": "25 Nov"},
    {"id": 6, "project": 2, "title": "Design onboarding screens", "status": "Done", "priority": "High", "assignee": 4, "due": "01 Nov"},
    {"id": 7, "project": 2, "title": "Set up push notification service", "status": "In Progress", "priority": "High", "assignee": 3, "due": "16 Nov"},
    {"id": 8, "project": 2, "title": "Offline data sync", "status": "In Progress", "priority": "High", "assignee": 3, "due": "28 Nov"},
    {"id": 9, "project": 2, "title": "Write test cases for login", "status": "To Do", "priority": "Medium", "assignee": 5, "due": "22 Nov"},
    {"id": 10, "project": 2, "title": "Profile screen UI", "status": "To Do", "priority": "Low", "assignee": 2, "due": "30 Nov"},
    {"id": 11, "project": 3, "title": "Gather requirements from sales", "status": "In Progress", "priority": "High", "assignee": 1, "due": "18 Nov"},
    {"id": 12, "project": 3, "title": "Design database schema", "status": "To Do", "priority": "Medium", "assignee": 3, "due": "30 Nov"},
    {"id": 13, "project": 4, "title": "Finalise logo variations", "status": "Done", "priority": "High", "assignee": 4, "due": "05 Oct"},
    {"id": 14, "project": 4, "title": "Publish guidelines PDF", "status": "Done", "priority": "Medium", "assignee": 1, "due": "15 Oct"},
]

STATUSES = ["To Do", "In Progress", "Done"]


def member(member_id):
    return next((m for m in TEAM if m["id"] == member_id), None)


def project(project_id):
    return next((p for p in PROJECTS if p["id"] == project_id), None)


def enrich_task(task):
    """Return a copy of a task with its assignee and project name filled in."""
    t = dict(task)
    t["assignee_obj"] = member(task["assignee"])
    p = project(task["project"])
    t["project_name"] = p["name"] if p else ""
    return t


def enrich_project(proj):
    """Return a copy of a project with member objects and task counts."""
    p = dict(proj)
    p["member_objs"] = [member(i) for i in proj["members"]]
    tasks = [t for t in TASKS if t["project"] == proj["id"]]
    p["task_total"] = len(tasks)
    p["task_done"] = len([t for t in tasks if t["status"] == "Done"])
    return p
