# attendance.py

import pandas as pd
from datetime import datetime
import os

class AttendanceSystem:

    def __init__(self):
        self.marked_names = set()
        self.date_today = datetime.now().strftime("%Y-%m-%d")
        self.file_path = f"attendance/attendance_{self.date_today}.csv"

        if not os.path.exists("attendance"):
            os.makedirs("attendance")

        if not os.path.isfile(self.file_path):
            df = pd.DataFrame(columns=["Name", "Date", "Time"])
            df.to_csv(self.file_path, index=False)

    def mark_attendance(self, name):

        if name == "Unknown":
            return "Unknown face - not recorded"

        if name in self.marked_names:
            return f"{name} already marked"

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        self.marked_names.add(name)

        new_data = pd.DataFrame([[name, date, time]],
                                columns=["Name", "Date", "Time"])

        new_data.to_csv(self.file_path, mode='a',
                        header=False, index=False)

        return f"{name} attendance marked at {time}"