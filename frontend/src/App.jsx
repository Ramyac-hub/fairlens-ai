 import { useState } from "react";
import HomePage from "./pages/Home";
import Analysis from "./pages/Analysis";
import Simulation from "./pages/Simulation";
import AIExplain from "./pages/AIExplain";
import MultiDomain from "./pages/MultiDomain";

export default function App() {
  const [page, setPage] = useState("home");

  return (
    <div>
      <button onClick={() => setPage("home")}>Home</button>
      <button onClick={() => setPage("analysis")}>Analysis</button>
      <button onClick={() => setPage("simulation")}>Simulation</button>
      <button onClick={() => setPage("ai")}>AI</button>
      <button onClick={() => setPage("multi")}>Multi</button>

      {page === "home" && <HomePage />}
      {page === "analysis" && <Analysis />}
      {page === "simulation" && <Simulation />}
      {page === "ai" && <AIExplain />}
      {page === "multi" && <MultiDomain />}
    </div>
  );
}