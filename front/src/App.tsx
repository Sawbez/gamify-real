import { useState } from "react";
import "./App.css";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import useFetch from "./useFetch";
import { User } from "./schema.ts";
import TaskBoard from "./taskboard.tsx";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./Layout.tsx";
import SignIn from "./Signin.tsx";
import SignUp from "./Signup.tsx";

const App = () => {
  let userInfo = useState<User | null>(null);

  return (
    <>
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout userInfo={userInfo}/>}>
          {/* <Route index element={<App />}></Route> */}
          <Route path="/signin" element={<SignIn userInfo={userInfo} />}></Route>
          <Route path="/signup" element={<SignUp userInfo={userInfo} />}></Route>
          <Route path="/taskboard" element={<TaskBoard />}></Route>
        </Route>
      </Routes>
      </BrowserRouter>
    </>
  );
};

export default App;
