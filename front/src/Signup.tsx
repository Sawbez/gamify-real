import React from "react";
import "./App.css";

const SignUp = () => {
  const login = (event: React.FormEvent<HTMLFormElement>) => {
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

export default SignUp;
