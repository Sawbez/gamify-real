import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./Signin.tsx";
import Layout from "./Layout.tsx";
import SignUp from "./Signup.tsx";
import { useState } from "react";
import { User } from "./schema.ts";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
