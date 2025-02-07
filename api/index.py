from fastapi import FastAPI, Query
import csv
import os

app = FastAPI()

# Load student marks from a CSV file
STUDENT_MARKS = {}

csv_file_path = os.path.join(os.path.dirname(__file__), "C:\Prema\6Jan25\Vercelapp\marks.csv")  # Ensure correct path

# Check if file exists before loading
if os.path.exists(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip header
        for row in reader:
            if len(row) >= 2:
                name, marks = row[0].strip(), row[1].strip()
                STUDENT_MARKS[name] = marks
else:
    print("Warning: marks.csv not found!")

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    return {n: STUDENT_MARKS.get(n, "Not found") for n in name}

