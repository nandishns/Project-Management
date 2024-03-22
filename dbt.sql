--query
SELECT * FROM Students;
SELECT * FROM Rooms;

-- count
SELECT COUNT(*) FROM Students;
SELECT COUNT(*) FROM Rooms;

-- index scan
SELECT * FROM Students WHERE RoomID = 101;

-- table scan
SELECT * FROM Students WHERE Name LIKE '%John%';

-- multitable join
SELECT *
FROM Students
JOIN Rooms ON Students.RoomID = Rooms.RoomID
JOIN Payments ON Students.StudentID = Payments.StudentID;

