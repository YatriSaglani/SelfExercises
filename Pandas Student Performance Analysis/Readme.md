# Pandas Practice Tasks — Student Performance Analysis

A complete **Pandas practical assignment** focused on creating, cleaning, transforming, analyzing, and combining student datasets using Python and Pandas.

## 📌 Project Overview

This project is based on a practical assignment covering the core concepts of **Pandas DataFrames and data analysis**.

The project uses student academic and attendance data to practice:

- DataFrame creation and exploration
- Selection and filtering
- Sorting
- Missing-value handling
- Duplicate handling
- Data types and date/time operations
- Aggregation and GroupBy
- `transform()`
- Pivot tables
- Re-indexing
- Altering labels and columns
- Merge and Join operations
- Categorical variables
- Student performance analysis

---

## 📂 Dataset

Create a `students.csv` file containing **30 students** with the following columns:

```text
id
name
age
gender
city
course
maths
python
pandas
numpy
attendance
joining_date
```

### Example Record

```text
1,Raj,21,Male,Rajkot,Python,78,85,82,75,92,2026-01-10
```
Do not add the spaces before/after comma [,].
The project also requires additional datasets for Merge and Join operations:

### `fees.csv`

```text
id
course_fee
paid
remaining
```

### Student Performance Data

For the Join task:

```text
id
name
course
```

and

```text
id
percentage
attendance
```

---

# 📚 Tasks Covered

## Task 1 — Pandas Basics

- Read the CSV file using Pandas
- Display the first 5 rows
- Display the last 5 rows
- Find total rows and columns
- Display column names
- Display `info()`
- Display `describe()` for numerical columns

## Task 2 — DataFrame Operations

- Display `name`, `age`, and `course`
- Display `maths`, `python`, `pandas`, and `numpy`
- Create `total`
- Create `percentage`
- Create `result`

### Result Criteria

```text
percentage >= 40 → Pass
percentage < 40  → Fail
```

## Task 3 — Filtering

Perform filtering for:

1. Age > 20
2. Age <= 20
3. Python course students
4. Rajkot students
5. Attendance > 90
6. Python marks > 80
7. Maths marks between 60 and 80
8. Python course AND attendance > 85
9. Rajkot OR Ahmedabad students
10. Percentage >= 75

## Task 4 — Sorting

- Sort age ascending
- Sort age descending
- Sort Python marks descending
- Sort percentage descending
- Sort attendance ascending
- Sort course ascending and percentage descending

## Task 5 — Missing Values

Add blank values to:

- `age`
- `city`
- `python`
- `attendance`

Then:

- Find missing values using `isnull()`
- Count missing values column-wise
- Display rows containing missing values
- Fill numerical missing values with mean
- Fill categorical missing values with mode
- Verify that no missing values remain

## Task 6 — Duplicate Data

Add 2–3 duplicate rows.

Perform:

- Find duplicate rows
- Count duplicates
- Display duplicates
- Remove duplicates
- Check final DataFrame shape

## Task 7 — Data Types

- Find datatype of every column
- Convert `age` to integer
- Convert `joining_date` to datetime
- Verify `joining_date` datatype
- Create `joining_year`
- Create `joining_month`

## Task 8 — Date & Time

- Extract year
- Extract month
- Extract day
- Sort by joining date
- Filter students who joined after `2026-01-01`
- Find students who joined in January

## Task 9 — Aggregation

Calculate:

- Average Maths
- Average Python
- Maximum Python
- Minimum Python
- Total students
- Average attendance
- Maximum percentage
- Minimum percentage

## Task 10 — GroupBy

### Course-wise

Calculate:

- Total students
- Average Maths
- Average Python
- Average Pandas
- Average Percentage

### City-wise

Calculate:

- Total students
- Average percentage
- Average attendance

### Gender-wise

Calculate:

- Total students
- Average percentage

## Task 11 — `transform()`

- Calculate each course's average Python marks using `transform()`
- Calculate each city's average percentage using `transform()`
- Create `course_avg_python`
- Compare each student's Python marks with their course average
- Label students as:
  - `Above Average`
  - `Below Average`

## Task 12 — Pivot Table

Create the following pivot tables:

### Pivot 1

```text
Index    → course
Values   → percentage
Function → mean
```

### Pivot 2

```text
Index    → city
Columns  → gender
Values   → percentage
Function → mean
```

### Pivot 3

```text
Index    → course
Columns  → gender
Values   → python
Function → mean
```

## Task 13 — Re-Indexing

- Make `id` the index
- Rename the index to `Student_ID`
- Apply a custom index
- Use `reset_index()`
- Change selected column order

## Task 14 — Altering Labels

Rename columns:

```text
name   → student_name
python → python_marks
pandas → pandas_marks
numpy  → numpy_marks
```

Then:

- Add a new column
- Delete an unnecessary column
- Change column order

## Task 15 — Merge

Create:

### `students.csv`

```text
id
name
course
city
```

### `fees.csv`

```text
id
course_fee
paid
remaining
```

Merge both DataFrames using `id` with:

- Inner Join
- Left Join
- Right Join
- Outer Join

## Task 16 — Join

Create Student Data:

```text
id
name
course
```

Create Performance Data:

```text
id
percentage
attendance
```

Use `join()` to combine both DataFrames.

## Task 17 — Categorical Variables

- Convert `course` to categorical datatype
- Find unique courses
- Find number of categories
- Display categories
- Change category order
- Sort by course category

### Suggested Category Order

```text
Python
Data Science
AI
Web Development
```

---

# 🏆 Final Challenge — Student Performance Analysis

Perform a complete analysis of the student dataset.

Find:

1. Highest-percentage student
2. Lowest-percentage student
3. Course with the highest average percentage
4. City with the highest average attendance
5. Course with the most students
6. Student with highest Python marks
7. Average attendance
8. Number of Pass students
9. Number of Fail students
10. Course-wise average performance
11. City-wise average performance
12. Gender-wise performance
13. Students performing above their course average
14. Month with the most new students
15. Final analysis in a clean DataFrame

---

# 🛠️ Skills Covered

This practical assignment covers:

```text
Creation
Exploration
Selection
Filtering
Sorting
Data Cleaning
Missing Values
Duplicates
Data Types
Dates & Time
Aggregation
GroupBy
Transform
Merge
Join
Pivoting
Re-indexing
Altering Labels
Categorical Variables
Performance Analysis
```

---

# 💻 Technologies Used

- **Python**
- **Pandas**
- **Jupyter Notebook**
- **CSV**

---

# 📁 Suggested Project Structure

```text
Pandas-Practice-Tasks/
│
├── students.csv
├── student_data.csv
├── fees.csv
│
├── aggregation.ipynb
├── altering_tables.ipynb
├── categorical_variables.ipynb
├── dataframe_operations.ipynb
├── datatypes.ipynb
├── date_time.ipynb
├── duplicate_rows.ipynb
├── filtering.ipynb
├── groupby.ipynb
├── join.ipynb
├── merge.ipynb
├── missing_values.ipynb
├── pandas_basics.ipynb
├── pivot_table.ipynb
├── re_indexing.ipynb
├── sorting.ipynb
├── Student_Perform_Analysis_FinalChallange.ipynb
├── transform.ipynb
│
└── README.md
```

---

# ⚙️ Installation

Make sure Python is installed.

Install Pandas and Jupyter Notebook:

```bash
pip install pandas jupyter
```

---

# ▶️ How to Run

### Using Jupyter Notebook

Open the project folder in the terminal and run:

```bash
jupyter notebook
```

Then open the required `.ipynb` file and run the cells.

### Using VS Code

1. Open the project folder in VS Code.
2. Open the required `.ipynb` notebook.
3. Select a Python kernel.
4. Run each cell in order.
5. Make sure the CSV files are available in the project folder.

---

# 🎯 Learning Objective

The main objective of this project is to build practical knowledge of **Pandas and DataFrame-based data analysis**.

By completing this assignment, you will learn how to work with real-world-style student data, clean it, transform it, analyze it, and generate meaningful performance insights.

---

# 👩‍💻 Author

**Yatri**

Computer Engineering Student | Data Science Student

---

⭐ **Pandas Practice Project — Student Performance Analysis**
