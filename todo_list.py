import webbrowser
from threading import Timer
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Initialize the task list
task_list = ["Wash a car", "Play cricket"]

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Webpage</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
            }
            a {
                text-decoration: none;
                color: #007BFF;
                border: 1px solid #007BFF;
                padding: 10px 20px;
                border-radius: 5px;
            }
            a:hover {
                background-color: #007BFF;
                color: #fff;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My Simple Webpage!</h1>
        <p>This is a basic webpage created using Flask in Python.</p>
        <a href="/todo">Go to ToDo List</a>
    </body>
    </html>
    '''

@app.route('/todo')
def view_todo_list():
    task_items = ''.join([f'<li>{task} <a href="/remove_task/{index}" style="color: red;">Remove</a></li>' for index, task in enumerate(task_list)])
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>ToDo List</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: #333;
            }}
            ul {{
                list-style-type: none;
                padding: 0;
            }}
            li {{
                background: #fff;
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            form {{
                margin-top: 20px;
            }}
            input[type="text"] {{
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                width: 300px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #007BFF;
                color: #fff;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #0056b3;
            }}
            a {{
                text-decoration: none;
                color: #007BFF;
                border: 1px solid #007BFF;
                padding: 5px 10px;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #007BFF;
                color: #fff;
            }}
        </style>
    </head>
    <body>
        <h1>Your ToDo List</h1>
        <ul>
            {task_items}
        </ul>
        <form action="/add_task" method="post">
            <input type="text" name="task" placeholder="New task">
            <input type="submit" value="Add Task">
        </form>
        <br>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        task_list.append(task)
    return redirect(url_for('view_todo_list'))

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    if 0 <= task_index < len(task_list):
        task_list.pop(task_index)
    return redirect(url_for('view_todo_list'))

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Start a timer to open the browser after a short delay
    Timer(1, open_browser).start()
    app.run(debug=True)

