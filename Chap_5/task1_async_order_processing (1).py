import asyncio


async def calculate_marks(future, marks):
    print("[System] Calculating total marks...")
    await asyncio.sleep(2)
    future.set_result(sum(marks))


async def assign_grade(future, total_marks):
    print("[System] Assigning grade...")
    await asyncio.sleep(2)

    if total_marks >= 80:
        grade = "A"
    elif total_marks >= 60:
        grade = "B"
    else:
        grade = "C"

    future.set_result(grade)


def show_result(future):
    print(f"✓ COMPLETED → Result: {future.result()}")


async def main():
    loop = asyncio.get_running_loop()

    marks = [85, 78, 90]

    total_future = loop.create_future()
    grade_future = loop.create_future()

    total_future.add_done_callback(show_result)
    grade_future.add_done_callback(show_result)

    await calculate_marks(total_future, marks)
    await assign_grade(grade_future, total_future.result())


asyncio.run(main())
