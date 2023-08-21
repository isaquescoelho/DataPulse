# DataPulse

DataPulse is a Python-based project designed to demonstrate the difference between sequential and parallel data fetching from an SQLite database. It uses multiprocessing to achieve parallel data retrieval, and it provides a clear comparison between the performance of both methods.

## Prerequisites

- Python 3.x
- SQLite3

## Setup

### Clone the repository:

```bash
git clone https://github.com/xonfps/DataPulse
cd DataPulse
```

### Install dependencies:

You'll need SQLite for this project.

```bash
pip install sqlite3
```

> Note: If SQLite is already bundled with your Python installation, you won't need to install it separately.

### Database Setup:

Before running the project, ensure the SQLite database and the users table are properly set up.

## Running the Project

Navigate to the project's root directory:

```bash
cd path/to/DataPulse
```

Run the main.py script:

```bash
python main.py
```

This will:

- Populate the database with up to 100,000 users (if not already populated).
- Fetch data in parallel and display the time taken.
- Fetch data sequentially and display the time taken.
- Print out the entire users table (use this feature cautiously with large datasets).

## Results

After running the main.py script, you should see a comparison of the time taken for both parallel and sequential data fetching. The program will also indicate which method took longer.
