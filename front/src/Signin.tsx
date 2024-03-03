import React from "react";
import "./App.css";

const SignIn = () => {
  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    //CHECK if it worked serverside, not clientside, if it works, create a session, then return SUCESS: true/false

    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    // Ensure you have a correct endpoint and method for your fetch call
    const response = await fetch(`/users/${username}`, {
      method: 'GET', // or 'POST', depending on your backend
      // headers: {}, // if you need to include headers
      // body: JSON.stringify(data), // if you need to include a body
    });
    console.log(await response);
    const data: {username: string, id: number} = await response.json(); // Assuming the response is JSON
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
