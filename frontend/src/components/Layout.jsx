import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <>
      <header className="header">
        <div className="container header-inner">
          <Link to="/" className="logo">
            <img src="/Group1.png" alt="NetPulse Logo" className="logo-img" />
            <span className="logo-text">NetPulse</span>
          </Link>
          <nav className="nav">
            <Link to="/">Главная</Link>
            <Link to="/agents">Агенты</Link>
          </nav>
        </div>
      </header>

      <main>{children}</main>

      <footer className="footer">
        <div className="container">
          <small>© 2025 NetPulse.</small>
        </div>
      </footer>
    </>
  );
}
