"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# Your code here...
# Home - Show all tasks
@app.route("/")
def home():
    return render_template("index.html", tasks=TASKS)

# Add Task Page
@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        new_id = len(TASKS) + 1
        title = request.form.get("title")
        status = request.form.get("status")
        priority = request.form.get("priority")

        TASKS.append({
            'id': new_id,
            'title': title,
            'status': status,
            'priority': priority
        })

        return redirect(url_for("home"))

    return render_template("add.html")

# Single Task Detail
@app.route("/task/<int:id>")
def task_detail(id):
    task = next((t for t in TASKS if t["id"] == id), None)
    return render_template("task.html", task=task)

# About Page
@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True)
