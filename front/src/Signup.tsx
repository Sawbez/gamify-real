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
    try {
      const response = await fetch(`http://localhost:5000/users/${username}`, {
        method: 'POST',
        
        // You might need to adjust this part based on how your backend expects the request
      });
      console.log(response);
      if (response.status !== 404) {
        alert("sign up success");
        const response2=await fetch(`http://localhost:5000/users/${username}`, {
          method: 'GET',
          
          // You might need to adjust this part based on how your backend expects the request
        });
        const data = await response2.json();

        setUserInfo(data);
        
        alert("sign in success!")
      } else {
        // Handle failure (e.g., user not found)
        
        console.error('Sign-in failed');
        
      }
    } catch (error) {
      console.error('Error during sign-in:', error);
    }
  };

  return (
    <>
      <h1 className="text-blue-800">Sign Up</h1>
      <form onSubmit={login}>
        <label>Username</label>
        <input type="text" name="username" />
        <button type="submit" className="bg-blue-500">Sign Up</button>
      </form>
    </>
  );
};
export default SignUp;
