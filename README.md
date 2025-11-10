# Student Management System

A comprehensive desktop-based student marks management application built with Python, Tkinter, and SQLite. This system allows educational institutions to manage student exam records across multiple terms (Quarterly, Half-Yearly, and Finals).

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Login Credentials](#login-credentials)
- [Screenshots & Interface](#screenshots--interface)
- [Important Notes](#important-notes)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The Student Management System is a GUI-based application designed to streamline the process of managing student examination records. The system supports three examination terms and stores marks for five subjects: English, Language, Chemistry, Physics, and Mathematics. Built as a semester project, it demonstrates practical implementation of database management and GUI development.

## ✨ Features

### Core Functionality
- **User Authentication**: Secure login system for students and administrators
- **Multi-Term Support**: Manage records across three examination terms
  - Quarterly Exams
  - Half-Yearly Exams
  - Final Exams
- **Student Records Management**:
  - View individual student marks by name and standard
  - Insert new student records with marks
  - Search and retrieve student information
- **Subject Tracking**: Track marks for 5 core subjects
  - English
  - Language (Second Language)
  - Chemistry
  - Physics
  - Mathematics
- **Grade-wise Organization**: Students organized by standards (10, 11, 12)
- **User-Friendly Interface**: Clean, intuitive Tkinter-based GUI with custom styling
- **Data Validation**: Input validation with error handling and user feedback
- **Pre-populated Database**: Comes with sample data for 30 students

### Technical Features
- SQLite database for reliable data persistence
- Modular code architecture
- Real-time data retrieval and display
- Error handling with message boxes
- Responsive window design

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework for desktop interface
- **SQLite3**: Lightweight database for data storage
- **ttk (Tkinter themed widgets)**: Enhanced UI components
- **Pathlib**: File path management

## 🗄️ Database Schema

The system uses three main tables in the SQLite database:

### Tables Structure

**1. Quaterly**
```sql
CREATE TABLE Quaterly (
    rollno VARCHAR(300),
    student_name VARCHAR(300),
    standard VARCHAR(300),
    english VARCHAR(300),
    language VARCHAR(300),
    chemistry VARCHAR(300),
    physics VARCHAR(300),
    maths VARCHAR(300)
);
```

**2. Half_Yearly**
- Same structure as Quaterly table

**3. Finals**
- Same structure as Quaterly table

### Sample Data
The database comes pre-populated with 30 students:
- 10 students in Standard 10
- 10 students in Standard 11
- 10 students in Standard 12

Each student has marks for all three examination terms.

## 📁 Project Structure

```
Simple_Student_Management/
├── Project/
│   └── GUI/
│       ├── Db/
│       │   └── Student.py              # Database initialization script
│       ├── Student Detail/
│       │   └── build/
│       │       ├── gui.py              # Student details display window
│       │       └── assets/             # UI assets for details window
│       ├── Student Insert/
│       │   └── build/
│       │       ├── gui.py              # Student insertion window
│       │       └── assets/             # UI assets for insert window
│       ├── Student Pagge/
│       │   └── build/
│       │       ├── StudentPage.py      # Student login page
│       │       ├── Student_gui.py      # Alternative student interface
│       │       └── assets/             # UI assets for student page
│       ├── build/
│       │   ├── Final.py                # Main application (FINAL VERSION)
│       │   ├── FrontView.py            # Login interface
│       │   ├── test.py                 # Database testing script
│       │   └── assets/                 # Main UI assets
│       ├── Student.db                  # SQLite database file
│       └── Students.db                 # Alternative database file
└── README.md
```

## 📦 Prerequisites

Before running the application, ensure you have:

- **Python 3.6 or higher** installed
- **Tkinter** (usually comes pre-installed with Python)
- **SQLite3** (comes built-in with Python)

### Verify Installation
```bash
# Check Python version
python --version

# Check if tkinter is installed
python -m tkinter

# SQLite3 is built into Python, no separate installation needed
```

## 🚀 Installation

### 1. Clone or Download the Repository
```bash
git clone https://github.com/r3tr0z1ay3r/Simple_Student_Management.git
cd Simple_Student_Management/Project/GUI
```

### 2. Initialize the Database
Run the database initialization script to create tables and populate sample data:

```bash
cd Db
python Student.py
cd ..
```

This will create `Student.db` with three tables and 30 student records.

### 3. Verify Asset Files
Ensure all asset folders contain the required image files:
- `build/assets/` - Contains `entry_1.png`, `entry_2.png`, `submit.png`
- `Student Detail/build/assets/` - Contains `box1.png` to `box7.png`, `back.png`
- `Student Insert/build/assets/` - Contains `box_insert1.png` to `box_insert7.png`, `insert.png`

## ⚙️ Configuration

### Database Configuration

The application uses `Student1.db` by default. If you need to change the database:

1. Open `build/Final.py`
2. Modify the database connection:
```python
con = sqlite3.Connection('YourDatabaseName.db')
```

### Asset Path Configuration

**CRITICAL**: The application uses relative paths for assets. Ensure you run the application from the correct directory:

```bash
cd Project/GUI/build
python Final.py
```

If you encounter image loading errors, verify the `relative_to_assets()` function in the code points to the correct assets folder.

## 💻 Usage

### Starting the Application

1. Navigate to the build directory:
```bash
cd Project/GUI/build
```

2. Run the main application:
```bash
python Final.py
```

### Login Screen

The application will open with a login interface:
- **User ID**: Enter username
- **Password**: Enter password
- Press **Enter** or click **Submit** to login

### Main Features Walkthrough

#### 1. **Fetch Student Marks**
   - After login, you'll see the Student Login window
   - Enter **Student Name** (e.g., "Aadithya", "Abhirami")
   - Enter **Standard** (10, 11, or 12)
   - Select **Exam Term** from dropdown:
     - Quaterly
     - Half_Yearly
     - Finals
   - Click **Fetch MarkList**
   - A new window displays all marks for the selected student

#### 2. **Insert New Student Record**
   - From the Student Login window, click **Insert MarkList**
   - Fill in the form:
     - Student Name
     - Student Grade (10, 11, or 12)
     - Exam Term (select from dropdown)
     - English marks
     - Language marks
     - Chemistry marks
     - Physics marks
     - Maths marks
   - Click **Insert** button
   - Success message confirms insertion

#### 3. **View Student Details**
   - The details window shows:
     - Student Name
     - Student Grade
     - Marks for all 5 subjects
   - Click **Back** to return to main menu

### Keyboard Shortcuts
- **Enter**: Submit login credentials

## 🔐 Login Credentials

Default credentials for testing:

### Student/Admin Access
```
Username: admin
Password: admin
```

> **Note**: The current version uses a simple dictionary-based authentication. For production use, implement proper user authentication with hashed passwords.

## 🖼️ Screenshots & Interface

### Window Specifications

1. **Login Window**: 800x600 pixels, grey background (#666666)
2. **Student Page**: 760x467 pixels, grey background (#838B8B)
3. **Student Detail Window**: 800x600 pixels, grey background (#666666)
4. **Insert Window**: 800x600 pixels, grey background (#666666)

All windows are non-resizable for consistent UI experience.

## ⚠️ Important Notes

### Asset Files
- **Required**: The application requires PNG image files for buttons and input boxes
- **Path Dependency**: All asset paths are relative to the execution directory
- **Missing Assets**: If assets are missing, the application will crash with a `TclError`

### Database Notes
- The database file must be in the same directory as `Final.py`
- Roll numbers are auto-generated based on existing records
- Student names are case-sensitive in searches
- Standards must be entered as numbers (10, 11, or 12)

### Known Limitations
1. No update or delete functionality (only insert and view)
2. Basic authentication system (not production-ready)
3. No data export functionality
4. Limited error handling for database constraints
5. No backup/restore features

### Best Practices
- Always run the database initialization script before first use
- Keep backup copies of the database file
- Ensure student names match exactly when searching (case-sensitive)
- Verify asset paths if moving the project to a different location

## 🔮 Future Enhancements

Potential improvements for the system:

- [ ] **Update/Delete Functionality**: Allow modification and deletion of records
- [ ] **Advanced Search**: Search by roll number, multiple filters
- [ ] **Report Generation**: Export marks to PDF/Excel
- [ ] **Data Analytics**: Calculate averages, class rankings, performance trends
- [ ] **Multi-user Roles**: Separate interfaces for students, teachers, and admins
- [ ] **Secure Authentication**: Implement proper password hashing and user management
- [ ] **Attendance Tracking**: Expand beyond marks to include attendance
- [ ] **Notification System**: Alert students about marks updates
- [ ] **Responsive Design**: Make windows resizable with dynamic layouts
- [ ] **Database Backup**: Automatic backup functionality
- [ ] **Bulk Import**: Import student data from CSV/Excel files

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m "Add: Your feature description"
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation for new features

## 📝 License

This project is an academic/educational submission developed for Semester 2. 

**Educational Use**: Feel free to use this project for learning purposes, educational assignments, or as a reference for similar projects.

For commercial use or redistribution, please contact the repository owner.

## 👤 Author

**r3tr0z1ay3r**
- GitHub: [@r3tr0z1ay3r](https://github.com/r3tr0z1ay3r)
- Project: Student Management System (Semester 2 Mini Project)

## 🙏 Acknowledgments

- **Tkinter Designer** by Parth Jadhav - Used for GUI design and generation
- **Python Community** - For excellent documentation and support
- **SQLite** - For providing a lightweight, reliable database solution
- All contributors and testers who helped improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Important Notes](#important-notes) section
2. Verify asset files are in place
3. Ensure database is properly initialized
4. Open an issue on GitHub with detailed error information

## 📚 Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer)

---



**Note**: This is an educational project developed for learning purposes. The system demonstrates fundamental concepts of GUI development and database management in Python.
