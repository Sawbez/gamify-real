import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./Signin.tsx";
import Layout from "./Layout.tsx";
import SignUp from "./Signup.tsx";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
    <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<App />}></Route>
          <Route path="/signin" element={<SignIn />}></Route>
          <Route path="/signup" element={<SignUp />}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
