def top_task(task_stack):
    if not task_stack:
        return None
    return task_stack[-1]

task_stack = ["task 1", "task 2", "task 3"]
print(top_task(task_stack))
