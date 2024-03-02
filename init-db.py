
"""
-- Categories Table
CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- 'Health/Foods', 'Work', 'Fitness'
);
-- Achievements Table
CREATE TABLE Achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    categoryId INTEGER,
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);
-- Users Table
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
);
-- User Experience Table
CREATE TABLE UserExperience (
    userId INTEGER,
    categoryId INTEGER,
    experience INTEGER NOT NULL,
    PRIMARY KEY (userId, categoryId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);
-- User Levels Table
CREATE TABLE UserLevels (
    userId INTEGER,
    categoryId INTEGER,
    level INTEGER NOT NULL,
    PRIMARY KEY (userId, categoryId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);
-- User Achievements Join Table
CREATE TABLE UserAchievements (
    userId INTEGER,
    achievementId INTEGER,
    PRIMARY KEY (userId, achievementId),
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (achievementId) REFERENCES Achievements(id)
);
-- Tasks Table
CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    categoryId INTEGER,
    FOREIGN KEY (userId) REFERENCES Users(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id)
);
-- Sub-Tasks Table
CREATE TABLE SubTasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    taskId INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY (taskId) REFERENCES Tasks(id)
);
"""

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

#we are done for now
connection.close()
