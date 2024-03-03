from dataclasses import dataclass, field

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Achievement:
    id: int
    name: str
    description: str
    points: int
    categoryId: int

@dataclass
class User:
    id: int
    username: str

@dataclass
class UserExperience:
    userId: int
    categoryId: int
    experience: int

@dataclass
class UserLevel:
    userId: int
    categoryId: int
    level: int

@dataclass
class UserAchievement:
    userId: int
    achievementId: int

@dataclass
class Task:
    id: int
    userId: int
    name: str
    description: str
    points: int
    categoryId: int

@dataclass
class SubTask:
    id: int
    taskId: int
    name: str
    description: str
    points: int
