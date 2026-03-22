# recognize.py

from attendance import AttendanceSystem
import time

# Create attendance system
attendance = AttendanceSystem()

# Simulated recognition (replace later with real camera)
names_detected = ["Dharshini", "Arun", "Dharshini", "Unknown"]

print("Starting Face Recognition...\n")

for name in names_detected:
    result = attendance.mark_attendance(name)
    print(result)
    time.sleep(1)

print("\nAttendance process completed.")