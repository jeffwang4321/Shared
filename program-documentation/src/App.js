import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./components/Home";
import Documentation from "./components/Documentation";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/documentation/:page" component={Documentation} />
      </Switch>
    </Router>
  );
};

export default App;
