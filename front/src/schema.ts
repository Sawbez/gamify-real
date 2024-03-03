interface Category {
  id: number;
  name: string;
}

interface Achievement {
  id: number;
  name: string;
  description: string;
  points: number;
  categoryId: number;
}

interface User {
  id: number;
  username: string;
}

interface UserExperience {
  userId: number;
  categoryId: number;
  experience: number;
}

interface UserLevel {
  userId: number;
  categoryId: number;
  level: number;
}

interface UserAchievement {
  userId: number;
  achievementId: number;
}

interface Task {
  id: number;
  userId: number;
  name: string;
  description: string;
  points: number;
  categoryId: number;
}

interface SubTask {
  id: number;
  taskId: number;
  name: string;
  description: string;
  points: number;
}
