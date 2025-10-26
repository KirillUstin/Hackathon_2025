// src/api/tasks.js

// ⚙️ Базовый URL API (можно вынести в .env позже)
const API_BASE = "http://localhost:8000/api";

// === Создание новой задачи ===
export async function createTask(target, checks) {
  try {
    const response = await fetch(`${API_BASE}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ target, checks }),
    });

    if (!response.ok) throw new Error("Ошибка при создании задачи");
    return await response.json();
  } catch (error) {
    console.error("Ошибка создания задачи:", error);
    throw error;
  }
}

// === Получение статуса задачи ===
export async function getTaskStatus(taskId) {
  try {
    const response = await fetch(`${API_BASE}/tasks/${taskId}`);
    if (!response.ok) throw new Error("Ошибка получения статуса");
    return await response.json();
  } catch (error) {
    console.error("Ошибка получения статуса:", error);
    throw error;
  }
}
