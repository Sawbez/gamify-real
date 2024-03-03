import React from "react";
import "./App.css";

const SignIn = () => {
  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    // Ensure you have a correct endpoint and method for your fetch call
    const response = await fetch(`/users/${username}/`, {
      method: 'GET', // or 'POST', depending on your backend
      // headers: {}, // if you need to include headers
      // body: JSON.stringify(data), // if you need to include a body
    });
    const data = await response.json(); // Assuming the response is JSON
    console.log(data); // Process the response data
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
