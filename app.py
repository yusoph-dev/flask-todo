import logging
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from rabbitmq_handler import RabbitMQHandler

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
rabbitmq_url = 'amqp://guest:guest@localhost:5672/'
exchange = 'logs'
routing_key = 'flask_log'
handler = RabbitMQHandler(rabbitmq_url, exchange, routing_key)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)  # Add this line

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route("/")
def home():
    # app.logger.info("Home page accessed")
    print("Home page accessed")
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    app.logger.info(f"Added new todo: {title}")
    # verify if app.logger.info(f"Added new todo: {title}") is working
    print(f"Added new todo: {title}")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    app.logger.info(f"Updated todo: {todo_id} - {todo.title}")
    print(f"Updated todo: {todo_id} - {todo.title}")
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    app.logger.info(f"Deleted todo: {todo_id} - {todo.title}")
    print(f"Deleted todo: {todo_id} - {todo.title}")
    return redirect(url_for("home"))

@app.route("/logs")
def view_logs():
    try:
        with open('logs.txt', 'r') as file:
            logs = file.read()
            print("logs", logs)
            app.logger.info(f"Viewed log files")
    except FileNotFoundError:
        logs = "No logs available."
        print("No logs available.")
    return render_template("logs.html", logs=logs)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)