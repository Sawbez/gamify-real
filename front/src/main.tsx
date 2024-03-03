import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./Signin.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
    <Routes>
        <Route path='/'>
          <Route index element={<App />}></Route>
          <Route path="/signin" element={<SignIn />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
