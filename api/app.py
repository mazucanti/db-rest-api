from flask import (
    Flask,
    redirect,
    request,
    render_template,
    url_for
)
from modules import (
    db_operations,
    metrics
)
from pathlib import Path
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
from uuid import uuid4

app = Flask(__name__)

DB_URL = "postgresql://{user}:{pswd}@db:5432/{db}".format(
    user=os.environ['POSTGRES_USER'],
    pswd=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB']
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['UPLOAD_FOLDER'] = '/api/data/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = uuid4().hex


db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def upload_data():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = Path(app.config['UPLOAD_FOLDER']) / filename
            if file_path.suffix != '.csv':
                return redirect(request.url)
            file.save(file_path)
        table = request.form['table']
        if table == '':
            return redirect(request.url)
        db_operations.insert_csv_table(db, file_path, table)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/hired_above_avg', methods=["GET"])
def render_table():
    table = metrics.hired_higher_than_avg(db)
    return render_template('hired_avg.html', table=table)

app.run(port=5000, host='0.0.0.0', debug=True)