import React from "react";

export default function AgentCard({ agent }) {
  const isOnline = agent.status === "online";
  return (
    <div className={`agent-card ${isOnline ? "online" : "offline"}`}>
      <h3>{agent.id}</h3>
      <p>📍 {agent.location}</p>
      <p>
        Статус:{" "}
        <span className={`status-dot ${isOnline ? "green" : "red"}`}>
          {isOnline ? "🟢 Онлайн" : "🔴 Оффлайн"}
        </span>
      </p>
      <small>Последнее обновление: {new Date(agent.last_seen).toLocaleString()}</small>
    </div>
  );
}
