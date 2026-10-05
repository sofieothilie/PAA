from database import add_todo, list_todos

tool_map = {
    "add_todo": add_todo,
    "list_todos": list_todos,
}

tools = list(tool_map.values())
