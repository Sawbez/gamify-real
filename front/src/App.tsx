import { useState } from "react";
import "./App.css";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import useFetch from "./useFetch";
import { User } from "./schema.ts";


type HelloSchema = {
  hello: string;
};

const App = ({signedin, userInfo} : {signedin:Boolean;userInfo: User | null; }) => {
  const [resp, loading] = useFetch<HelloSchema>("/hw");
  const [count, setCount] = useState(0);

  if (!resp && !loading) {
    return <h1>Error {String(resp)} 🤕</h1>;
  }

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1 id="test" className="text-green-500">
        {loading ? "loading" : resp?.hello}
      </h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
};

export default App;
