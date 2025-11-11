def attendance_status(total_working_days, days_absent, threshold=75):
    if total_working_days <= 0:
        return "Invalid total working days"
    attendance = total_working_days - days_absent
    percent = (attendance / total_working_days) * 100
    status = "Eligible to sit in the exam" if percent >= threshold else "Not eligible to sit in the exam"
    return {
        "attendance": attendance,
        "percent": percent,
        "status": status
    }

print(attendance_status(60, 12))