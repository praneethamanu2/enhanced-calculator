# 🧮 Enhanced Calculator – Command-Line Application

An advanced command-line **Calculator Application** built in Python that supports multiple arithmetic operations, undo/redo functionality, persistent history management, and real-time logging using design patterns (Factory, Memento, and Observer).  
This project also includes **automated testing and CI/CD integration** using **GitHub Actions**.

---

## 📘 Project Description

This calculator extends basic arithmetic operations with advanced functionality and modern software engineering principles.

### ✨ Features

- **Arithmetic Operations**
  - Add, Subtract, Multiply, Divide
  - Power, Root, Modulus, Integer Division
  - Percentage, Absolute Difference
- **Factory Pattern** – Dynamically create operation functions.
- **Memento Pattern** – Undo/Redo support for history state.
- **Observer Pattern** – Automatic logging and history autosave.
- **History Management**
  - View, Clear, Undo, Redo, Save, Load.
- **Configurable Environment**
  - Control precision, max input size, file directories, and autosave.
- **Comprehensive Logging**
  - Every operation and error is logged.
- **Test Coverage**
  - 100% test coverage with `pytest` and `pytest-cov`.
- **Continuous Integration (CI)**
  - Automated testing and coverage enforcement via GitHub Actions.

---

## ⚙️ Installation Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/enhanced-calculator.git
2️⃣ Create a Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🧾 Configuration Setup

This project uses a .env file for configuration (loaded using python-dotenv).

📄 Example .env File

Create a file named .env in the project root with the following contents:

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=4
CALCULATOR_MAX_INPUT_VALUE=1e9
CALCULATOR_DEFAULT_ENCODING=utf-8


These variables control where logs and history are stored, how precise your calculations are, and whether the calculator autosaves history to CSV.

💻 Usage Guide

Run the calculator in the terminal:

python main.py

Available Commands
Command	Description
add a b	Add two numbers
subtract a b	Subtract second number from the first
multiply a b	Multiply two numbers
divide a b	Divide first number by second
power a b	Raise a to the power of b
root a b	Take the b-th root of a
modulus a b	Remainder of a divided by b
int_divide a b	Integer division result (no decimals)
percent a b	Compute (a / b) * 100
abs_diff a b	Absolute difference between a and b
history	View previous calculations
clear	Clear the history
undo	Undo the last calculation
redo	Redo the last undone calculation
save	Save current history to CSV
load	Load history from CSV
help	Show all available commands
exit	Exit the calculator

Example session:

calc> add 5 10
= 15.0
calc> divide 20 5
= 4.0
calc> undo
Undone.
calc> redo
Redone.
calc> history
[2025-11-01T17:30Z] divide(20, 5) = 4.0

🧪 Testing Instructions
Run Unit Tests
pytest

Run Tests with Coverage
pytest --cov=app --cov-report=term-missing


✅ Expected output:

----------- coverage: platform darwin, python 3.12 -----------
Name                        Stmts   Miss  Cover
---------------------------------------------------------
app/                         ...     ...   100%
---------------------------------------------------------
TOTAL                         ...     0   100%
======================== 30 passed in 0.6s ========================


All tests must pass

Coverage must be ≥ 90% (your project achieves 100%)

🔄 CI/CD – GitHub Actions

This project includes a continuous integration workflow that automatically:

Checks out the code.

Sets up the Python environment.

Installs dependencies.

Runs unit tests with coverage.

Fails the build if coverage < 90%.

📂 Workflow File

Located at:

.github/workflows/python-app.yml

🧠 Example Workflow Summary
name: Python application
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - run: pytest --cov=app --cov-fail-under=90


Every time you push or create a pull request, this workflow runs automatically in the Actions tab on GitHub.
cd enhanced-calculator

