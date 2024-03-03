/*
Synopsis:

```ts
type Categories = "Health/Foods" | "Work" | "Fitness"

interface Achievement {
    name: string;
    description: string;
    points: number;
};

interface User {
    username: string;
    experience: Record<Categories, number>;
    level: Record<Categories, number>;
    achievements: Achievement[];
};

type Leaderboard = Record<Categories, User[]>;

```
*/

-- Categories Table
CREATE TABLE IF NOT EXISTS Categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE -- 'Health/Foods', 'Work', 'Fitness'
);

-- Achievements Table
CREATE TABLE IF NOT EXISTS Achievements (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    categoryId INTEGER,
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);

-- Users Table
CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE
);

-- User Experience Table
CREATE TABLE IF NOT EXISTS UserExperience (
    userId INTEGER,
    categoryId INTEGER,
    experience INTEGER NOT NULL,
    PRIMARY KEY (userId, categoryId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);

-- User Levels Table
CREATE TABLE IF NOT EXISTS UserLevels (
    userId INTEGER,
    categoryId INTEGER,
    level INTEGER NOT NULL,
    PRIMARY KEY (userId, categoryId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);

-- User Achievements Join Table
CREATE TABLE IF NOT EXISTS UserAchievements (
    userId INTEGER,
    achievementId INTEGER,
    PRIMARY KEY (userId, achievementId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (achievementId) REFERENCES Achievements(id)
);

-- Tasks Table
CREATE TABLE IF NOT EXISTS Tasks (
    id SERIAL PRIMARY KEY,
    userId INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    categoryId INTEGER,
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);

-- Sub-Tasks Table
CREATE TABLE IF NOT EXISTS SubTasks (
    id SERIAL PRIMARY KEY,
    taskId INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY (taskId) REFERENCES Tasks(id)
);
