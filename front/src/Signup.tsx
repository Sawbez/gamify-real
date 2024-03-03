import React from "react";
import "./App.css";
import { Dispatch, SetStateAction } from "react";
import { User } from "./schema.ts";


const SignUp = ({ userInfo }:{
  userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
}) => {

  const [userInfoVal, setUserInfo] = userInfo;
  
  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    console.log(username); // Process username here

  };

  return (
    <>
      <h1 className="text-blue-800"
      >Sign in</h1>
      <form onSubmit={login}>
        <label>Username</label>
        <input type="text" name="username" />
        <button type="submit" className="bg-blue-500">Sign in</button>
      </form>
    </>
  );
};
export default SignUp;
