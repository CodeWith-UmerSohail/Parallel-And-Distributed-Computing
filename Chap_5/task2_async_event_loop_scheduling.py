import asyncio
import time
import random


def monitor_heart_rate(end_time, loop):
    print("❤️  [HEART] Checking patient's heart rate...")

    time.sleep(random.randint(1, 3))
    heart_rate = random.randint(60, 120)

    print(f"   ✓ Heart rate: {heart_rate} BPM")

    if loop.time() + 1 < end_time:
        print("   → Scheduling: Blood Pressure Check in 1 second...\n")
        loop.call_later(1, check_blood_pressure, end_time, loop)
    else:
        shutdown(loop)


def check_blood_pressure(end_time, loop):
    print("🩸 [BP] Measuring blood pressure...")

    time.sleep(random.randint(1, 3))
    systolic = random.randint(100, 140)
    diastolic = random.randint(60, 90)

    print(f"   ✓ BP: {systolic}/{diastolic} mmHg")

    if loop.time() + 1 < end_time:
        print("   → Scheduling: Medicine Reminder in 1 second...\n")
        loop.call_later(1, medicine_reminder, end_time, loop)
    else:
        shutdown(loop)


def medicine_reminder(end_time, loop):
    medicines = ["Paracetamol", "Insulin", "Antibiotic"]
    med = random.choice(medicines)

    print("💊 [MEDICINE] Checking medicine schedule...")

    time.sleep(random.randint(1, 3))
    print(f"   ✓ Reminder: Give {med} to patient")

    if loop.time() + 1 < end_time:
        print("   → Scheduling: Heart Rate Monitoring in 1 second...\n")
        print("-" * 50)
        loop.call_later(1, monitor_heart_rate, end_time, loop)
    else:
        shutdown(loop)


def shutdown(loop):
    print("\n⏰ Monitoring time completed. System shutting down...")
    loop.stop()


if __name__ == "__main__":
    print("=" * 60)
    print("    HOSPITAL PATIENT MONITORING SYSTEM")
    print("    Using Asyncio Event Loop Scheduling")
    print("=" * 60)

    loop = asyncio.get_event_loop()
    end_time = loop.time() + 30  # run for 30 seconds

    loop.call_soon(monitor_heart_rate, end_time, loop)
    loop.run_forever()
    loop.close()

    print("\nSystem safely stopped. All data recorded.")
