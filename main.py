import yaml
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()


def load_tasks() -> dict:
    with open("builds/tasks.yaml", "r") as file:
        tasks_data = yaml.safe_load(file)
    return tasks_data


def load_builds() -> dict:
    with open("builds/builds.yaml", "r") as file:
        builds_data = yaml.safe_load(file)
    return builds_data


def sort_tasks(build_name: str, tasks_data: dict, builds_data: dict) -> List[str]:
    tasks = tasks_data.get("tasks", [])
    builds = builds_data.get("builds", [])

    # Создаем словарь для быстрого доступа к задачам по имени
    tasks_dict = {task["name"]: task for task in tasks}

    # Проверяем наличие указанного билда
    build = next((b for b in builds if b["name"] == build_name), None)
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")

    # Рекурсивная функция для сортировки задач с учетом зависимостей
    def sort_dependencies(task_name, dependencies, sorted_tasks, visited):
        if task_name in visited:
            raise HTTPException(status_code=400, detail="Cyclic dependency detected")

        visited.add(task_name)

        if task_name not in sorted_tasks:
            dependencies = dependencies or []
            for dependency in dependencies:
                sort_dependencies(dependency, tasks_dict.get(dependency, {}).get("dependencies", []), sorted_tasks,
                                  visited)
            sorted_tasks.append(task_name)

        visited.remove(task_name)

    sorted_tasks = []
    visited = set()

    # Сортируем задачи для указанного билда
    for task in build.get("tasks", []):
        sort_dependencies(task, tasks_dict.get(task, {}).get("dependencies", []), sorted_tasks, visited)

    return sorted_tasks


@app.post("/get_tasks")
def get_tasks(request_data: dict):
    build_name = request_data.get("build")
    tasks_data = load_tasks()
    builds_data = load_builds()

    try:
        sorted_tasks = sort_tasks(build_name, tasks_data, builds_data)
        return sorted_tasks
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
