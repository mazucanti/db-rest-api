from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/database/<table_name>')
def update_database(table_name):
    pass

def retrieve_data():
    pass

@app.route('/analysis/<int:year>', methods=['GET'])
def employees_hired_dept(year):
    data = summarize_year_dept(year)
    return data
    

def _read_db(year):
    pass

def summarize_year_dept(year):
    data = _read_db(year)

app.run(port=5000, host='0.0.0.0', debug=True)