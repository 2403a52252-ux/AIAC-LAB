-- Create Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Class VARCHAR(20)
);

-- Create Courses table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50),
    TotalClasses INT
);

-- Create Attendance table
CREATE TABLE Attendance (
    AttendanceID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    AttendanceDate DATE,
    IsPresent BIT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert sample data into Students
INSERT INTO Students VALUES
(1, 'John', 'Doe', 'Class-A'),
(2, 'Jane', 'Smith', 'Class-A'),
(3, 'Mike', 'Johnson', 'Class-B'),
(4, 'Sarah', 'Williams', 'Class-B'),
(5, 'Tom', 'Brown', 'Class-A');

-- Insert sample data into Courses
INSERT INTO Courses VALUES
(1, 'Mathematics', 40),
(2, 'Science', 35),
(3, 'English', 30);

-- Insert sample attendance data
INSERT INTO Attendance VALUES
(1, 1, 1, '2024-01-01', 1),
(2, 1, 1, '2024-01-02', 1),
(3, 1, 1, '2024-01-03', 0),
(4, 2, 1, '2024-01-01', 1),
(5, 2, 1, '2024-01-02', 0),
(6, 3, 1, '2024-01-01', 0),
(7, 3, 1, '2024-01-02', 0),
(8, 4, 1, '2024-01-01', 1),
(9, 5, 1, '2024-01-01', 0);

-- Query to find students with attendance below 75%
SELECT 
    s.StudentID,
    s.FirstName,
    s.LastName,
    c.CourseName,
    COUNT(a.AttendanceID) as TotalPresent,
    co.TotalClasses,
    (CAST(COUNT(CASE WHEN a.IsPresent = 1 THEN 1 END) AS FLOAT) / co.TotalClasses * 100) as AttendancePercentage
FROM 
    Students s
    JOIN Attendance a ON s.StudentID = a.StudentID
    JOIN Courses c ON a.CourseID = c.CourseID
    JOIN Courses co ON a.CourseID = co.CourseID
GROUP BY 
    s.StudentID, s.FirstName, s.LastName, c.CourseName, co.TotalClasses
HAVING 
    (CAST(COUNT(CASE WHEN a.IsPresent = 1 THEN 1 END) AS FLOAT) / co.TotalClasses * 100) < 75
ORDER BY 
    AttendancePercentage DESC;