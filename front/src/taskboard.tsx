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

      console.log(task)
      const response = await fetch(`http://localhost:5000/users/${userInfoVal?.username}/tasks`,{
            method: 'POST',
            body: JSON.stringify(task),
            headers: {
              'Content-Type': 'application/json',
            },
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
              <input name="name" type="text"/>
              <label>Desc</label>
              <input name="description" type="text" />
              <label>Category</label>
              <input type="number" name="categoryId" />
              <button type="submit">create task</button>
            </form>


          </>
        ) : (<>
        <p>nothing here :)</p>
        <div className="atask">
          <h2>Quests</h2>
          <p>Write your tasks!</p>
          <p>points 10</p>
          <p>cateogory "cooking"</p>
          <button>finished this</button>
        </div>
      </>)}


  
      <button className="bg-lime-600"onClick={()=> {getTask()}}>click me!</button>
    </>
  );
};
export default TaskBoard;
