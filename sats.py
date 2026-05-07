# =========================================================
# STUDENT ATTENDANCE TRACKING SYSTEM (SATS)
# PROG103 – Structured Programming Assignment
# Developed by: Francess M kamara
# =========================================================

from datetime import datetime

# -------------------------------
# CONSTANTS
# -------------------------------

MAX_STUDENTS = 100
VALID_STATUSES = ["present", "absent", "late"]


# -------------------------------
# FUNCTION: DISPLAY HEADER
# -------------------------------

def display_header():
    print("\n" + "=" * 65)
    print("        STUDENT ATTENDANCE TRACKING SYSTEM (SATS)")
    print("=" * 65)


# -------------------------------
# FUNCTION: GET STUDENT DETAILS
# -------------------------------

def get_student_details():
    """
    Collects student information from the user.
    """

    print("\n--- Enter Student Details ---")

    student_name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    course = input("Enter course/module name: ").strip()

    return student_name, student_id, course


# -------------------------------
# FUNCTION: MARK ATTENDANCE
# -------------------------------

def mark_attendance():
    """
    Allows the user to mark attendance status.
    """

    while True:

        status = input(
            "Enter attendance status (Present / Absent / Late): "
        ).strip().lower()

        if status in VALID_STATUSES:
            return status
        else:
            print("Invalid status! Please enter Present, Absent, or Late.")


# -------------------------------
# FUNCTION: GENERATE REMARK
# -------------------------------

def generate_remark(status):
    """
    Generates attendance remark based on status.
    """

    if status == "present":
        return "Excellent attendance"

    elif status == "late":
        return "Needs punctuality improvement"

    else:
        return "Absent from class"


# -------------------------------
# FUNCTION: DISPLAY RECORD
# -------------------------------

def display_record(record):
    """
    Displays processed attendance record.
    """

    print("\n" + "-" * 50)
    print("           ATTENDANCE RECORD")
    print("-" * 50)

    print(f"Student Name : {record['name']}")
    print(f"Student ID   : {record['id']}")
    print(f"Course       : {record['course']}")
    print(f"Date         : {record['date']}")
    print(f"Status       : {record['status'].title()}")
    print(f"Remark       : {record['remark']}")

    print("-" * 50)


# -------------------------------
# FUNCTION: DISPLAY SUMMARY
# -------------------------------

def display_summary(records):
    """
    Displays all attendance records entered.
    """

    print("\n" + "=" * 70)
    print("                 ATTENDANCE SUMMARY")
    print("=" * 70)

    if len(records) == 0:
        print("No attendance records available.")
        return

    present_count = 0
    absent_count = 0
    late_count = 0

    for record in records:

        print(
            f"{record['name']} ({record['id']}) | "
            f"{record['course']} | "
            f"{record['status'].title()} | "
            f"{record['date']}"
        )

        if record['status'] == "present":
            present_count += 1

        elif record['status'] == "absent":
            absent_count += 1

        elif record['status'] == "late":
            late_count += 1

    print("\n" + "-" * 70)

    print(f"Total Present : {present_count}")
    print(f"Total Absent  : {absent_count}")
    print(f"Total Late    : {late_count}")

    print("=" * 70)


# -------------------------------
# FUNCTION: MAIN PROGRAM
# -------------------------------

def main():

    attendance_records = []

    display_header()

    while True:

        # Get student details
        name, student_id, course = get_student_details()

        # Mark attendance
        status = mark_attendance()

        # Generate remark
        remark = generate_remark(status)

        # Get current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store attendance record
        record = {
            "name": name,
            "id": student_id,
            "course": course,
            "status": status,
            "remark": remark,
            "date": current_date
        }

        attendance_records.append(record)

        # Display individual record
        display_record(record)

        # Ask user to continue
        choice = input(
            "\nDo you want to record another attendance? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            break

    # Display final summary
    display_summary(attendance_records)

    print("\nThank you for using SATS.")
    print("System Closed Successfully.")


# -------------------------------
# PROGRAM EXECUTION
# -------------------------------

if __name__ == "__main__":
    main()