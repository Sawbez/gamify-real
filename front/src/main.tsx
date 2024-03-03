import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SignIn from "./Signin.tsx";
import Layout from "./Layout.tsx";
import SignUp from "./Signup.tsx";
import { useState } from "react";


const App2 = () =>{
  const [signedin, setSignedIn] = useState(false)
  const [userInfo,setUserInfo] = useState<User|null>(null)

  return (
    <BrowserRouter>
    <Routes>
        <Route path='/' element={<Layout signedin={signedin} setSignedIn={setSignedIn} userInfo={userInfo}/>}>
          <Route index element={<App signedin={signedin} userInfo={userInfo}/>}></Route>
          <Route path="/signin" element={<SignIn setSignedIn={setSignedIn} setUserInfo={setUserInfo}/>}></Route>
          <Route path="/signup" element={<SignUp setSignedIn={setSignedIn} setUserInfo={setUserInfo}/>}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App2 />
  </React.StrictMode>
);
