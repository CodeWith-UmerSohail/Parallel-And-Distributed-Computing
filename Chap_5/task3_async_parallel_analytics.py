import asyncio


@asyncio.coroutine
def analyze_student_enrollment(total_students):
    """
    Task 1: Student Enrollment Analysis

    Calculates total enrolled students semester-wise.
    """
    enrolled = 0

    for semester in range(1, total_students + 1):
        enrolled += semester * 10
        print(f"🎓 [ENROLLMENT] Semester {semester}: {semester*10} students enrolled")
        yield from asyncio.sleep(1)

    print(f"\n✅ [ENROLLMENT COMPLETE] Total Enrolled Students = {enrolled}\n")


@asyncio.coroutine
def calculate_faculty_workload(num_faculty):
    """
    Task 2: Faculty Workload Calculation

    Calculates teaching load for each faculty member.
    """
    total_hours = 0

    for i in range(1, num_faculty + 1):
        hours = i * 3
        total_hours += hours
        print(f"🧑‍🏫 [FACULTY] Faculty {i}: Teaching {hours} hours/week")
        yield from asyncio.sleep(1)

    print(f"\n✅ [FACULTY COMPLETE] Total Teaching Hours = {total_hours}\n")


@asyncio.coroutine
def process_exam_results(num_students):
    """
    Task 3: Exam Result Processing

    Processes exam results and calculates pass percentage.
    """
    passed = 0

    for i in range(1, num_students + 1):
        marks = i * 7
        if marks >= 40:
            passed += 1
        print(f"📝 [RESULTS] Student {i}: Marks = {marks}")
        yield from asyncio.sleep(1)

    pass_percentage = (passed / num_students) * 100
    print(f"\n✅ [RESULTS COMPLETE] Pass Percentage = {pass_percentage:.1f}%\n")


if __name__ == "__main__":
    print("=" * 65)
    print("    UNIVERSITY MANAGEMENT ANALYTICS SYSTEM")
    print("    Using Asyncio Parallel Tasks")
    print("=" * 65)
    print("\nRunning analytics tasks in PARALLEL:\n")

    tasks = [
        asyncio.Task(analyze_student_enrollment(6)),
        asyncio.Task(calculate_faculty_workload(5)),
        asyncio.Task(process_exam_results(8))
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    print("=" * 65)
    print("    ALL UNIVERSITY ANALYTICS COMPLETED")
    print("=" * 65)
