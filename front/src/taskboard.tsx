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

    async function addTask(event: React.FormEvent<HTMLFormElement>){
      event.preventDefault();
      const formData = new FormData(event.currentTarget);
      const task:Task = {
        id:42069,
        userId: userInfoVal?.id!,
        name: formData.get("name")?.toString()!,
        description: formData.get("description")?.toString()!,
        points:10,
        categoryId: Number.parseInt(formData.get("categoryId")?.toString()!),
      }
      const response = await fetch(`http://localhost:5000/tasks/${userInfoVal?.id}`,{
            method: 'POST',
            body: JSON.stringify(task),
        });

      if (response.ok) {
        alert("item added!");
      }
    }

  return (
    <>

      {userInfoVal ? (
        <>
          <h1>{"this is a taskboard :) "}</h1>
          {tasks.length > 0 ? tasks.map((task) => (
              <div className="atask"key={task.id}>
                <h2>name {task.name}</h2>
                <p> desc {task.description}</p>
                <p> points {task.points}</p>
                <p> category {task.categoryId}</p>
              </div>
            )) : <p>No tasks</p>}


            <form onSubmit={addTask}>
              <h2>create a task</h2>
              <label>name</label>
              <input name="name"></input>
              <label>Desc</label>
              <input name="description"></input>
              <label>Category</label>
              <input name="categoryId"></input>
              <input type="submit">add Task</input>
            </form>

        </>
      ) : (<><p>{"nothing here :)"}</p><div className="atask">
      <h2>name coolName</h2>
      <p> desc some description</p>
      <p id="points">points 10</p>
      <p id="category">cateogory "cooking"</p>
      <button>finished this</button>
    </div></>)
      }
      <h1>{"this is a taskboard :)"} {userInfo?.username}</h1>
      <button className="bg-lime-600"onClick={()=> {getTask()}}>click me!</button>
    </>
  );
};
export default TaskBoard;
