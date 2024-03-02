import { useState } from "react";
import "./App.css";
import useFetch from "./useFetch";

type HelloSchema = {
  hello: string;
};

const SignIn = () => {
  const [resp, loading] = useFetch<HelloSchema>("/hw");
  const [count, setCount] = useState(0);

  if (!resp && !loading) {
    return <h1>Error {String(resp)} 🤕</h1>;
  }

  return (
    <>
      <h1>
        Sign in
      </h1>
      
      <form>
        <label>Username</label>
        <input type="text"></input>
        <input type="submit">Sign in</input>
      </form>
      
    </>
  );
};

export default SignIn;
