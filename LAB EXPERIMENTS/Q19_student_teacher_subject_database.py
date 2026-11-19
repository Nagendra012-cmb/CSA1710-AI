records = [
    {"student":"Arun", "teacher":"Dr. Rao", "subject":"AI", "code":"CS401"},
    {"student":"Kiran", "teacher":"Ms. Priya", "subject":"Python", "code":"CS402"},
    {"student":"Sita", "teacher":"Mr. Kumar", "subject":"DBMS", "code":"CS403"}
]
for r in records:
    print(f"{r['student']} | {r['teacher']} | {r['subject']} | {r['code']}")
print("\nStudents enrolled in Python:")
for r in records:
    if r["subject"] == "Python": print(r["student"])
