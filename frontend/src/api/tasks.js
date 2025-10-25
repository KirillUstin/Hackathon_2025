// frontend/src/api/tasks.js
import client from './client'

export const createTask = (task) => client.post('/api/tasks', task)
export const getTask = (taskId) => client.get(`/api/tasks/${taskId}`)
