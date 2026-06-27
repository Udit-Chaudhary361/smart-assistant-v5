from flask import request , redirect , render_template , Flask , url_for
from app.database import Database
from app.tools.joke_tool import get_joke
database = Database()

app = Flask(__name__)

@app.route("/" , methods=["GET"])
def home():
    return render_template(
        "home.html"
    )

@app.route("/name" , methods = ["GET" , "POST"])
def name():
    error = None
    if request.method == "POST":
        named = request.form["added_name"].strip()
        if named:
            database.set_name(named)
            return redirect(url_for('name'))
        else:
            error = "Name Can't Be Empty"
    current_name = database.get_name()
    return render_template(
        "name.html",
        current_name=current_name,
        error=error)

@app.route("/notes" , methods=["GET" , "POST"])
def notes():
    error = None
    if request.method == "POST":
        note_name = request.form["added_note"].strip()
        if note_name:
            database.add_note(note_name)
            return redirect(url_for('notes'))
        else:
            error = "Note Can't Be Empty"
    all_notes = database.get_notes()
    return render_template(
        "notes.html",
        all_notes=all_notes,
        error=error)

@app.route("/notes/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    database.delete_note(note_id)
    return redirect(
        url_for("notes")
    )

@app.route("/notes/edit_note/<int:note_id>" , methods=["POST" , "GET"])
def edit_note(note_id):
    error = None
    if request.method == "POST":
        new_note = request.form["note"].strip()
        if not new_note:
            error = "Note Cannot Be Empty"
        else:
            database.update_note(note_id,new_note)
            return redirect(url_for("notes"))
    note_name = database.get_note_by_id(note_id)
    return render_template(
        "edit_note.html",
        note_id=note_id,
        note_name=note_name,
        error=error)
@app.route("/tasks" , methods = ["GET" , "POST"])
def tasks():
    error = None
    if request.method == "POST":
        task = request.form["task"].strip()
        if not task:
            error = "Task Can't Be Empty"
        else:
            database.add_task(task)
            return redirect(url_for("tasks"))
    all_tasks = database.get_tasks()
    return render_template(
        "tasks.html",
        all_tasks=all_tasks,
        error=error
    )

@app.route("/tasks/delete/<task_id>" , methods=["POST"])
def delete_task(task_id):
    database.delete_task(task_id)
    return redirect(
        url_for('tasks')
    )

@app.route("/tasks/edit/<task_id>" , methods = ["GET" , "POST"])
def edit_task(task_id):
    error = None
    if request.method == "POST":
        new_task = request.form["task"].strip()
        if not new_task:
            error = "Task Cannot Be Empty"
        else:
            database.update_task(task_id,new_task)
            return redirect(url_for("tasks"))
    task_name = database.get_task_by_id(task_id)
    return render_template(
        "edit_task.html",
        task_id=task_id,
        task_name=task_name,
        error=error)

@app.route("/task/completed/<task_id>" , methods=["GET" , "POST"])
def completed(task_id):
    database.complete_task(task_id)
    return redirect(
        url_for("tasks")
    )

@app.route("/joke", methods=["GET", "POST"])
def joke():
    jokes=None
    if request.method == "POST":
        jokes = get_joke()

    return render_template(
        "joke.html",
        jokes=jokes
    )

@app.route("/history" , methods=["GET"])
def history():
    history= database.history_viewer()
    history = history.replace("\n", "<br>")
    return render_template(
        "history.html",
        history=history
    )

app.run(debug=True)