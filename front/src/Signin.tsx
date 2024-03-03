import React from "react";
import "./App.css";
import { Dispatch, SetStateAction } from "react";
import { User } from "./schema.ts";


const SignIn = ({setSignedIn, setUserInfo }: {
  setSignedIn:Dispatch<SetStateAction<boolean>>;
  setUserInfo:Dispatch<SetStateAction<User|null>>;
  }) => {
  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    console.log(username); // Process username here
  };

  return (
    <>
      <h1>Sign in</h1>
      <form onSubmit={login}>
        <label>Username</label>
        <input type="text" name="username" />
        <button type="submit">Sign in</button>
      </form>
    </>
  );
};

export default SignIn;
