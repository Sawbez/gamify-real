import React from "react";
import "./App.css";

const SignUp = () => {
  const signuup = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    // Ensure you have a correct endpoint and method for your fetch call
    const response = await fetch(`/users/${username}`, {
      method: 'POST', // or 'POST', depending on your backend
      // headers: {}, // if you need to include headers
      // body: JSON.stringify(data), // if you need to include a body
    });
    console.log(await response);
    const data = await response.json(); // Assuming the response is JSON
    alert(data); // Process the response data
  };

  return (
    <>
      <h1>Sign up</h1>
      <form onSubmit={signuup}>
        <label>Username</label>
        <input type="text" name="username" />
        <button type="submit">Sign up</button>
      </form>
    </>
  );
};

export default SignUp;
