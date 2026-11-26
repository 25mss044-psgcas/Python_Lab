# Python Programming Lab Experiments

A collection of 15 Python programming experiments covering fundamental programming concepts, data structures, numerical computing, object-oriented programming, exception handling, and database connectivity.

This repository contains practical implementations designed for Python Programming Laboratory coursework and academic learning.

## 📚 Experiments Included

| No. | Experiment Title |
|---:|---|
| 01 | Operators and Operator Precedence |
| 02 | Conditional Statements and Loops |
| 03 | NumPy Array Creation and Matrix Operations |
| 04 | Indexing, Slicing, and Reshaping Multi-Dimensional NumPy Arrays |
| 05 | String Operations |
| 06 | List Operations and List Comprehensions |
| 07 | Tuple Operations and Nested Tuples |
| 08 | Dictionaries and Student Record Management System |
| 09 | Function Arguments and Multiple Return Values |
| 10 | Recursive Functions (Factorial and Fibonacci) |
| 11 | Inheritance, Method Overriding, and Operator Overloading |
| 12 | Handling Built-In Exceptions |
| 13 | Handling User-Defined Exceptions |
| 14 | MySQL Database Connection and Table Creation |
| 15 | CRUD Operations on MySQL Using Parameterized Queries |

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Numerical Computing:** NumPy
- **Database:** MySQL
- **Database Connectivity:** MySQL Connector/Python

## ⚙️ Requirements

- Python 3.x
- NumPy
- MySQL Server
- MySQL Connector/Python (required for Experiments 14 and 15)

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd <repository-directory>
```

### 3. Install Required Dependencies

```bash
pip install numpy mysql-connector-python
```

### 4. Execute the Programs

Run an individual experiment using:

```bash
python experiment_01.py
```

Replace the filename with the corresponding experiment you want to execute.

## 🗄️ Database Configuration

Experiments 14 and 15 require a running MySQL server.

Before executing these programs:

1. Install and start MySQL Server.
2. Create the database named `college_db`.
3. Update the MySQL connection credentials in the Python programs.
4. Ensure that the MySQL Connector/Python package is installed.

Example:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)
```

**Note:** Replace the sample credentials with your own local MySQL configuration. Do not commit real database passwords or other sensitive credentials to a public repository.

## 🎯 Learning Objectives

These experiments provide practical exposure to:

- Python operators and control-flow statements.
- Arrays, matrices, and numerical operations using NumPy.
- Python strings and built-in data structures.
- Functions, recursion, and argument handling.
- Object-oriented programming principles.
- Built-in and user-defined exception handling.
- Relational database connectivity.
- SQL operations and parameterized queries.

## 📁 Repository Structure

A suggested organization for the programs:

```text
Python-Programming-Lab/
│
├── README.md
├── LICENSE
│
├── experiment_01.py
├── experiment_02.py
├── experiment_03.py
├── experiment_04.py
├── experiment_05.py
├── experiment_06.py
├── experiment_07.py
├── experiment_08.py
├── experiment_09.py
├── experiment_10.py
├── experiment_11.py
├── experiment_12.py
├── experiment_13.py
├── experiment_14.py
└── experiment_15.py
```

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions of the MIT License.

See the [LICENSE](LICENSE) file for the complete license terms.

## 👨‍💻 Author

**Author:** [SANJAY M / 25MSS044]

**Repository:** Python Programming Lab Experiments

---

*Built for learning, practicing, and exploring Python programming concepts.*
