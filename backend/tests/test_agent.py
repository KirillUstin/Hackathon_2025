# tests/test_agent.py
import time

def fake_agent_loop(task_list):
    """Имитация цикла агента"""
    processed = []
    for task in task_list:
        print(f"Processing task {task}")
        time.sleep(0.05)  # имитация работы
        processed.append(task)
    return processed

def test_fake_agent_loop():
    tasks = [1,2,3]
    results = fake_agent_loop(tasks)
    assert results == tasks
