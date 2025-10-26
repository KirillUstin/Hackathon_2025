import React, { useState, useEffect } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [tcpPort, setTcpPort] = useState("");
  const [checks, setChecks] = useState({
    http: false,
    ping: false,
    dns: false,
    tcp: false,
    traceroute: false,
  });
  const [results, setResults] = useState([]);
  const [taskId, setTaskId] = useState(null);
  const [status, setStatus] = useState("idle");

  // 🟦 При загрузке страницы проверяем, есть ли сохранённая задача
  useEffect(() => {
    const savedTaskId = localStorage.getItem("lastTaskId");
    if (savedTaskId) {
      setTaskId(savedTaskId);
    }
  }, []);

  const handleToggle = (type) => {
    setChecks((prev) => ({ ...prev, [type]: !prev[type] }));
  };

  const handleSubmit = async () => {
    if (query.trim() === "") {
      alert("Введите адрес или домен для проверки!");
      return;
    }

    const selectedChecks = Object.entries(checks)
      .filter(([_, value]) => value)
      .map(([key]) => key.toUpperCase());

    if (selectedChecks.length === 0) {
      alert("Выберите хотя бы один тип проверки!");
      return;
    }

    if (checks.tcp && tcpPort.trim() === "") {
      alert("Введите порт для TCP-проверки!");
      return;
    }

    setStatus("loading");

    const fakeTaskId = Math.random().toString(36).substring(2, 10);
    setTaskId(fakeTaskId);
    localStorage.setItem("lastTaskId", fakeTaskId);

    // Эмуляция проверки
    setTimeout(() => {
      const fakeResults = selectedChecks.map((type) => {
        if (type === "DNS") {
          return {
            type,
            details: {
              A: "192.168.1.10",
              AAAA: "2001:0db8::1",
              MX: "mail.example.com",
              NS: "ns1.example.com",
              TXT: "v=spf1 include:_spf.google.com ~all",
            },
          };
        }

        if (type === "TRACEROUTE") {
          return {
            type,
            hops: [
              { hop: 1, ip: "192.168.1.1", time: "1.2" },
              { hop: 2, ip: "10.0.0.1", time: "4.3" },
              { hop: 3, ip: "8.8.8.8", time: "15.6" },
              { hop: 4, ip: "142.250.186.46", time: "21.8" },
            ],
          };
        }

        return {
          type,
          status: Math.random() > 0.2 ? "Успешно" : "Ошибка",
          time: (Math.random() * 200).toFixed(1) + " мс",
          ...(type === "TCP PORT" && { port: tcpPort }),
        };
      });

      setResults(fakeResults);
      setStatus("done");
    }, 1500);
  };

  return (
    <section className="hero">
      <div className="hero-content">
        <h1>NetPulse</h1>
        <p>
          Онлайн-сервис для проверки доступности сайтов, IP и DNS-записей —
          быстро и удобно.
        </p>

        {/* Поле ввода адреса */}
        <div className="search-box">
          <input
            type="text"
            placeholder="Введите домен или IP..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="search-input"
          />
          <button onClick={handleSubmit} className="search-btn">
            {status === "loading" ? "Проверяем..." : "Начать проверку"}
          </button>
        </div>

        {/* Выбор проверки */}
        <div className="check-options">
          {["http", "ping", "dns", "tcp", "traceroute"].map((type) => (
            <div
              key={type}
              className={`check-tile ${checks[type] ? "active" : ""}`}
              onClick={() => handleToggle(type)}
            >
              <span className="check-label">
                {type === "tcp"
                  ? "TCP Port"
                  : type === "traceroute"
                  ? "Traceroute"
                  : type.toUpperCase()}
              </span>
            </div>
          ))}
        </div>

        {/* Поле для TCP-порта */}
        {checks.tcp && (
          <div className="tcp-input">
            <input
              type="number"
              placeholder="Введите порт (например, 80)"
              value={tcpPort}
              onChange={(e) => setTcpPort(e.target.value)}
            />
          </div>
        )}

        {taskId && (
          <p style={{ color: "#93c5fd", marginTop: "20px" }}>
            ID задачи: <b>{taskId}</b>
          </p>
        )}

        {/* Результаты */}
        {results.length > 0 && (
          <div className="results-section-inner">
            <h2>Результаты проверки</h2>
            <div className="results-grid">
              {results.map((res, i) => (
                <div key={i} className="result-card animated">
                  <h3>{res.type}</h3>

                  {/* DNS */}
                  {res.type === "DNS" && (
                    <div className="dns-results">
                      {Object.entries(res.details).map(([key, value]) => (
                        <p key={key}>
                          <b>{key}:</b> {value}
                        </p>
                      ))}
                    </div>
                  )}

                  {/* Traceroute */}
                  {res.type === "TRACEROUTE" && (
                    <div className="trace-results">
                      <table>
                        <thead>
                          <tr>
                            <th>№ Хопа</th>
                            <th>IP-адрес</th>
                            <th>Время (мс)</th>
                          </tr>
                        </thead>
                        <tbody>
                          {res.hops.map((hop) => (
                            <tr key={hop.hop}>
                              <td>{hop.hop}</td>
                              <td>{hop.ip}</td>
                              <td>{hop.time}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}

                  {/* Остальные проверки */}
                  {res.type !== "DNS" && res.type !== "TRACEROUTE" && (
                    <>
                      {res.port && <p>Порт: {res.port}</p>}
                      <p>Статус: {res.status}</p>
                      <p>Время отклика: {res.time}</p>
                    </>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </section>
  );
}
