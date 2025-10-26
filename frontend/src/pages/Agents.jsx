import React from "react";

export default function Agents() {
  const agents = [
    { name: "Москва-01", status: "online", ip: "192.168.1.2", ping: "22 мс" },
    { name: "СПб-02", status: "offline", ip: "192.168.1.3", ping: "—" },
    { name: "Новосибирск-03", status: "online", ip: "192.168.1.4", ping: "31 мс" },
  ];

  return (
    <section className="agents-page">
      <div className="agents-overlay">
        <div className="agents-content">
          <h1>Активные агенты</h1>

          <div className="agents-list">
            {agents.map((agent, index) => (
              <div key={index} className="agent-card">
                <h3>{agent.name}</h3>
                <p>IP: {agent.ip}</p>
                <p>
                  Статус:{" "}
                  <span
                    className={`status ${
                      agent.status === "online" ? "online" : "offline"
                    }`}
                  >
                    {agent.status === "online" ? "Онлайн" : "Оффлайн"}
                  </span>
                </p>
                <p>Пинг: {agent.ping}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
