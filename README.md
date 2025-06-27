#  Design Patterns in Python

This repository contains implementations of commonly used design patterns in Python, with real-world examples and clean, modular code.

---

##  Patterns Implemented

###  Factory Method Pattern
- **Location:** `factory/report_exporter.py`
- **Description:** Implements a factory method for generating different types of report exporters (PDF, CSV, JSON) using class-based object creation and Open/Closed Principle.

###  Builder Pattern
- **Location:** `builder/resume_builder.py`
- **Description:** Uses the Builder Pattern to construct complex `Resume` objects step-by-step using a fluent API. Solves the telescoping constructor problem.

###  Singleton Pattern
- **Location:** `singleton/` *
- **Description:** Ensures only one instance of an object exists across the app. Implemented for a SchoolBell and Cricket Scoreboard example using `__new__()`.

---

##  Usage

Each pattern is located in its own folder and includes:
- Example code
- Explanation in comments
- Entry point for testing (if applicable)

Run the files using:
```bash
python folder_name/file_name.py
