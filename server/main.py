import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template_string, request
from nonogram import nonogram_ga

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Nonogram 5x5</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 10px;
        }
        input {
            width: 50px;
        }
        table {
            border-collapse: collapse;
        }
        td {
            width: 50px;
            height: 50px;
            border: 1px solid black;
        }
        .black {
            background-color: black;
        }
        .white {
            background-color: white;
        }
    </style>
</head>
<body>
    <h1>Nonogram</h1>
    <form method="POST">
        <table>
            <thead>
                <tr>
                    <th></th>
                    {% for col in range(5) %}
                        <th>
                            <input type="text" name="col{{ col }}" placeholder="Col {{ col+1 }}" value="{{ request.form.get('col' + col|string, '') }}">
                        </th>
                    {% endfor %}
                </tr>
            </thead>
            <tbody>
                {% for row in range(5) %}
                    <tr>
                        <th>
                            <input type="text" name="row{{ row }}" placeholder="Row {{ row+1 }}" value="{{ request.form.get('row' + row|string, '') }}">
                        </th>
                        {% for col in range(5) %}
                            <td class="{{ 'black' if grid and grid[row][col] == 1 else 'white' if grid and grid[row][col] == 0 else '' }}"></td>
                        {% endfor %}
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        columns = {f"col{col}": request.form.get(f"col{col}") for col in range(5)}
        rows = {f"row{row}": request.form.get(f"row{row}") for row in range(5)}        
        col = convert_data(columns)
        r = convert_data(rows)
        nonogram_data = [col, r]
        result = nonogram_ga(nonogram_data)
        print(result)

    return render_template_string(HTML_TEMPLATE, grid=result)

def convert_data(data):
    result = []
    for key, value in data.items():
        if value:
            int_list = list(map(int, value.split()))
            result.append(int_list)
        else:
            result.append([])
    return result

if __name__ == '__main__':
    app.run(debug=True)
