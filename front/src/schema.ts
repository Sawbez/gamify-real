export interface Category {
  id: number;
  name: string;
}

export interface Achievement {
  id: number;
  name: string;
  description: string;
  points: number;
  categoryId: number;
}

export interface User {
  id: number;
  username: string;
}

export interface UserExperience {
  userId: number;
  categoryId: number;
  experience: number;
}

export interface UserLevel {
  userId: number;
  categoryId: number;
  level: number;
}

export interface UserAchievement {
  userId: number;
  achievementId: number;
}

export interface Task {
  id: number;
  userId: number;
  name: string;
  description: string;
  points: number;
  categoryId: number;
}

export interface SubTask {
  id: number;
  taskId: number;
  name: string;
  description: string;
  points: number;
}
