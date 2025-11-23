import csv
from datetime import datetime
import os


assignments = []

def get_input(prompt, validate):
    """General input function for validation."""
    while True:
        value = input(prompt)
        if validate(value):
            return value
        print("Invalid input. Try again.")

def is_valid_grade(value):
    try:
        grade = float(value)
        return 0 <= grade <= 100
    except ValueError:
        return False

def is_valid_weight(value):
    try:
        return float(value) > 0
    except ValueError:
        return False

def is_valid_category(value):
    return value.upper() in ['FA', 'SA']

# Ask user to input
while True:
    name = input("Assignment Name: ")
    category = get_input("Category (FA/SA): ", is_valid_category).upper()
    grade = float(get_input("Grade (0-100): ", is_valid_grade))
    weight = float(get_input("Weight: ", is_valid_weight))

    assignments.append({
        "name": name,
        "category": category,
        "grade": grade,
        "weight": weight,
        "weighted_grade": (grade / 100) * weight
    })

    cont = input("Add another assignment? (y/n): ").lower()
    if cont != 'y':
        break

# Calculation and Pass/Fail Logic

total_FA = sum(a["weighted_grade"] for a in assignments if a["category"] == "FA")
total_SA = sum(a["weighted_grade"] for a in assignments if a["category"] == "SA")

#Grade and GPA calculations
total_grade = total_FA + total_SA
gpa = (total_grade / 100) * 5.0 
gpa = round(gpa, 4)

# Calculating if the students Passed/Fail 
fa_weight_total = sum(a["weight"] for a in assignments if a["category"] == "FA")
sa_weight_total = sum(a["weight"] for a in assignments if a["category"] == "SA")

# Pass/Fail logic
fa_pass = total_FA >= (fa_weight_total / 2) if fa_weight_total > 0 else True
sa_pass = total_SA >= (sa_weight_total / 2) if sa_weight_total > 0 else True
status = "PASS" if fa_pass and sa_pass else "FAIL"

#Results format
print("\n--- RESULTS ---")
print(f"Total Formative: {total_FA:.2f} / {fa_weight_total:.0f}")
print(f"Total Summative: {total_SA:.2f} / {sa_weight_total:.0f}")
print(f"Total Grade: {total_grade:.2f} / {fa_weight_total + sa_weight_total:.0f}")
print(f"GPA: {gpa}")
print(f"Status: {status}")



with open("grades.csv", "w", newline="") as csvfile:
    fieldnames = ["Assignment", "Category", "Grade", "Weight"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for a in assignments:
        writer.writerow({
            "Assignment": a["name"], 
            "Category": a["category"],
            "Grade": a["grade"],
            "Weight": a["weight"]
        })

print("\ngrades.csv file created successfully!")

