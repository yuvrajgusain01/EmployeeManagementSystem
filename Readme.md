# Employee Management System

A simple Employee Management System built using Python and JSON. It allows users to manage employee records through a menu-driven program.

## Features

- Add employee details
- View all employees in a table
- Update employee details
- Delete employees using Employee ID
- Store employee data in a JSON file
- Handle invalid user input

## Technologies Used

- Python
- JSON

## Project Structure

```text
miniProject/
├── emp.py
├── storage.py
├── main.py
└── data.json
```

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the parent directory of `miniProject`.
3. Run the following command:

```bash
python -m miniProject.main
```

## Employee Details

The system stores the following information:

- Employee ID
- Employee Name
- Employee Age
- Employee Salary

Employee records are saved in `data.json` and remain available when the program is run again.

