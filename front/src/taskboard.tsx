import "./App.css";
import { User } from "./schema.ts";


const TaskBoard = ({userInfo}:{userInfo:User|null}) =>{

  return (
    <>
      <h1>this is a taskboard :) {userInfo?.username}</h1>
    </>
  );
};
export default TaskBoard;
