import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Documentation from "./components/Documentation";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" exact element={<Home />} />
        <Route path="/documentation/:page" element={<Documentation />} />
      </Routes>
    </Router>
  );
};

export default App;
