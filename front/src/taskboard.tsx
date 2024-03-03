import { json } from "react-router-dom";
import "./App.css";
import { User } from "./schema.ts";
import { Task } from "./schema.ts";
import { useState } from "react";
import { useEffect } from 'react';

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

    useEffect(()=> {getTask()});

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

    async function finishedTask(taskId: number) {
      try {
        const response = await fetch(`http://localhost:5000/users/${userInfoVal!.username}/tasks/${taskId}`, {
          method: 'DELETE', // Use the DELETE HTTP method to request the deletion of a resource
          headers: {
            'Content-Type': 'application/json',
          },
        });
    
        if (response.ok) {
          // If the delete was successful, filter out the deleted task from the local state
          setTasks(tasks.filter(task => task.id !== taskId));
          alert("Task successfully deleted!");
        } else {
          // Handle non-successful responses
          alert("Failed to delete the task.");
        }
      } catch (error) {
        console.error("Error deleting task:", error);
        alert("Error deleting task.");
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
                  <p id="points"> points {task.points}</p>
                  <p id="category"> category {task.categoryId}</p>
                  <button className="bg-lime-600" onClick={() => finishedTask(task.id)}>finished</button>

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
        
      </>)}
    </>
  );
};
export default TaskBoard;
