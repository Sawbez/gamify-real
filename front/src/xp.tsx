import React from "react";
import "./App.css";
import { User } from "./schema.ts";
import { useState } from "react";


const Xp = ({ userInfo }:{
    userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
  }) => {
    const [userInfoVal, setUserInfo] = userInfo;

    const getXP = async function(){
        console.log("hi");
        const response = await fetch(`/http://localhost:5000/users/${userInfoVal?.username}/experience`, {
            method:"GET";
        })
    }
    getXP();
    return (
        <h1>here's your xp </h1>
        
    )
}

export default Xp;