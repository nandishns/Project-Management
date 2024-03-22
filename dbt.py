import mysql.connector
import random
from faker import Faker

fake = Faker()

# Database configuration
db_config = {
    'user': 'root',
    'password': 'nasa@sql!123',
    'host': 'localhost',
    'database': 'dbt24_a1_pes1ug21cs364_nandish',
    'raise_on_warnings': True
}

# Establish a connection to the database
conn = mysql.connector.connect(**db_config)
c = conn.cursor()

def create_tables():
    # Students table
    c.execute('''CREATE TABLE IF NOT EXISTS Students (
                StudentID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Email VARCHAR(255),
                Phone VARCHAR(255)
            )''')

    # Rooms table
    c.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                RoomID INT AUTO_INCREMENT PRIMARY KEY,
                RoomNumber VARCHAR(255),
                Capacity INT,
                StudentId INT,
                FOREIGN KEY(StudentId) REFERENCES Students(StudentID) ON DELETE CASCADE
            )''')

    # Staff table
    c.execute('''CREATE TABLE IF NOT EXISTS Staff (
                StaffID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Role VARCHAR(255),
                Contact VARCHAR(255)
            )''')

    # Payments table
    c.execute('''CREATE TABLE IF NOT EXISTS Payments (
                PaymentID INT AUTO_INCREMENT PRIMARY KEY,
                StudentID INT,
                Amount DECIMAL(10,2),
                PaymentDate DATE,
                PaymentFor VARCHAR(255),
                FOREIGN KEY(StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE
            )''')

    # MaintenanceRequests table
    c.execute('''CREATE TABLE IF NOT EXISTS MaintenanceRequests (
                RequestID INT AUTO_INCREMENT PRIMARY KEY,
                RoomID INT,
                Description TEXT,
                RequestDate DATE,
                Status VARCHAR(255),
                FOREIGN KEY(RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
            )''')

    conn.commit()

def insert_data():
    # Insert fake students
    for _ in range(10000):
        c.execute("INSERT INTO Students (Name, Email, Phone) VALUES (%s, %s, %s)",
                  (fake.name(), fake.email(), fake.phone_number()))
    conn.commit()

    # Insert a predefined student
    c.execute("INSERT INTO Students (Name, Email, Phone) VALUES (%s, %s, %s)",
              ("NANDISH_PES1UG21CS364", "pes1202102665@pesu.pes.edu", fake.phone_number()))
    conn.commit()  # Commit to get the StudentID of the inserted student.

    # Get all student IDs
    c.execute("SELECT StudentID FROM Students")
    student_ids = [item[0] for item in c.fetchall()]

    # Insert fake rooms
    for _ in range(10000):
        c.execute("INSERT INTO Rooms (RoomNumber, Capacity, StudentId) VALUES (%s, %s, %s)",
                  (fake.building_number(), random.randint(1, 4), random.choice(student_ids)))
    conn.commit()

def insert_staff():
    roles = ['Manager', 'Receptionist', 'Housekeeper', 'Maintenance', 'Chef']
    for _ in range(10):
        c.execute("INSERT INTO Staff (Name, Role, Contact) VALUES (%s, %s, %s)",
                  (fake.name(), random.choice(roles), fake.phone_number()))
    conn.commit()

def insert_payments():
    payment_for_options = ['Room Charge', 'Maintenance Fee', 'Laundry Service', 'Food Service']
    # Assuming student_ids list is available from insert_data()
    c.execute("SELECT StudentID FROM Students")
    student_ids = [item[0] for item in c.fetchall()]
    for _ in range(10):
        c.execute("INSERT INTO Payments (StudentID, Amount, PaymentDate, PaymentFor) VALUES (%s, %s, %s, %s)",
                  (random.choice(student_ids), round(random.uniform(100.00, 1000.00), 2), fake.date(), random.choice(payment_for_options)))
    conn.commit()

def insert_maintenance_requests():
    statuses = ['Pending', 'In Progress', 'Completed']
    c.execute("SELECT RoomID FROM Rooms")
    room_ids = [item[0] for item in c.fetchall()]
    for _ in range(10):
        c.execute("INSERT INTO MaintenanceRequests (RoomID, Description, RequestDate, Status) VALUES (%s, %s, %s, %s)",
                  (random.choice(room_ids), fake.sentence(), fake.date(), random.choice(statuses)))
    conn.commit()

# Execute the functions
create_tables()
insert_data()
insert_staff()
insert_payments()
insert_maintenance_requests()

# Close the connection
conn.close()