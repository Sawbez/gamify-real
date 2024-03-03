import React from "react";
import "./App.css";
import { Dispatch, SetStateAction,useState } from "react";
import { User } from "./schema.ts";
import  { Redirect } from 'react-router-dom'


const SignIn = ({ setSignedIn, setUserInfo }: {
  setSignedIn: Dispatch<SetStateAction<boolean>>;
  setUserInfo: Dispatch<SetStateAction<User | null>>;
}) => {

  const [redirectToHome, setRedirectToHome] = useState(false);

  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get("username");
    console.log(username); // Debugging line to see the username

    // Assuming the backend is adjusted to handle sign-in
    try {
      const response = await fetch(`/users/${username}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        // You might need to adjust this part based on how your backend expects the request
      });
      const data = await response.json();

      if (response.ok) {
        alert("sign in sucess!");
        setSignedIn(true);
        setUserInfo(data); // Assuming the response includes user info
        setRedirectToHome(true);
      } else {
        // Handle failure (e.g., user not found)
        
        console.error('Sign-in failed:', data.message);
        setSignedIn(false);
        setUserInfo(null);
        
      }
    } catch (error) {
      console.error('Error during sign-in:', error);
    }
  };

  if (redirectToHome) {
    return <edirect to="/" />;
  }

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