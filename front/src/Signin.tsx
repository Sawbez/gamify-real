import React from "react";
import "./App.css";
import { User } from "./schema.ts";
import { useState } from "react";

const SignIn = ({ userInfo }:{
  userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
}) => {

  const [userInfoVal, setUserInfo] = userInfo;

  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    console.log("hi pls work");
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    console.log(username); // Debugging line to see the username

    // Assuming the backend is adjusted to handle sign-in
    try {
      const response = await fetch(`http://localhost:5000/users/${username}`, {
        method: 'GET',
        
        // You might need to adjust this part based on how your backend expects the request
      });
      console.log(response);
      const data = await response.json();
      console.log(data);
      if (data["username"]) {
        alert("sign in sucess!");
        setUserInfo(data);
        console.log("sign in success!")
      } else {
        // Handle failure (e.g., user not found)
        
        console.error('Sign-in failed:', data.message);
        
      }
    } catch (error) {
      console.error('Error during sign-in:', error);
    }
  };

  return (
    <>
      <h1>Sign in</h1>
      
      <form onSubmit={login}>
        <label>Username</label>
        <input type="text" name="username" />
        <button type="submit" >Sign in</button>
      </form>
    </>
  );
};

export default SignIn;