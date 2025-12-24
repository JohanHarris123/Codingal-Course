import matplotlib.pyplot as plt

students_names = ["Sanjay", "Rahul", "Karan", "Wasin", "Ramesh", "Ajay", "Sartay", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

marks_perc = [(mark / 50) * 100 for mark in students_marks]

def marks_line_chart():
    plt.plot(students_names, students_marks, marker='o', linestyle='-', color='blue', ms=20, mec='r', linewidth=20)
    plt.plot(students_names, students_marks, marker='o', linestyle='dotted', color='orange', ms=10, mec='b', linewidth=5)
    plt.title("Students Marks Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Marks out of 50")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='green')
    plt.title("Students Percentage Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

marks_line_chart()
percentage_bar_chart()