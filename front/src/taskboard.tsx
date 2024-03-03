import "./App.css";
import { User } from "./schema.ts";


const TaskBoard = ({userInfo}:{userInfo:User|null}) =>{

    async function getTask() {
        const response = await fetch("/tasks/",{
            method: 'GET'
        });
        const tasks = await response.json()
        console.log(tasks);
    }

  return (
    <>
      <h1>this is a taskboard :) {userInfo?.username}</h1>
      <button onClick={getTask()}>click me!</button>
    </>
  );
};
export default TaskBoard;
