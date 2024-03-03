import { json } from "react-router-dom";
import "./App.css";
import { User } from "./schema.ts";
import { Task } from "./schema.ts";
import { useState } from "react";

const TaskBoard = ({ userInfo }:{
  userInfo: [User | null, React.Dispatch<React.SetStateAction<User | null>>]
}) => {
  const [userInfoVal, setUserInfo] = userInfo;
  const [tasks,setTasks] = useState<Task[]>([]);

    async function getTask() {
      if (userInfoVal){
        const response = await fetch(`http://localhost:5000/tasks/${userInfoVal?.id}`,{
            method: 'GET'
        });
        const tasksThing = await response.json()
        setTasks(tasksThing);
        console.log(tasks);
      }
    }

    getTask(); 

    async function addTask(){
      const task:Task = {
        id:42069,
        userId: userInfoVal?.id!,
        name:"example name",
        description:"example desc",
        points:10,
        categoryId:2
      }
      const response = await fetch(`http://localhost:5000/tasks/${userInfoVal?.id}`,{
            method: 'POST',
            body: JSON.stringify(task),
        });
    }

  return (
    <>
      {userInfoVal ? (
        <>
          <h1>this is a taskboard :) </h1>
          {tasks.length > 0 ? tasks.map((task) => (
              <div className="atask"key={task.id}>
                <h2>name {task.name}</h2>
                <p> desc {task.description}</p>
                <p> points {task.points}</p>
                <p> category {task.categoryId}</p>
              </div>
            )) : <p>No tasks</p>}

            <form>
              <label>name</label>
              <input name="name"></input>
              <label>Desc</label>
              <input name="description"></input>
              <label>Category</label>
              <input name="categoryId"></input>
            </form>
        </>
      ) : (<><p>nothing here :)</p><div className="atask">
      <h2>name coolName</h2>
      <p> desc some description</p>
      <p>points 10</p>
      <p>cateogory "cooking"</p>
      <button>finished this</button>
    </div></>)
      }
    </>
  );
};
export default TaskBoard;
