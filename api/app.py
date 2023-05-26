from flask import (
    Flask,
    flash,
    redirect,
    request,
    render_template
)
from modules import (
    db_operations,
    metrics
)
from pathlib import Path
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DB_URL = "postgresql://{user}:{pswd}@0.0.0.0:5432/{db}".format(
    user=os.environ['POSTGRES_USER'],
    pswd=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB']
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['UPLOAD_FOLDER'] = '/api/data/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def insert_csv_table():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file found')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = Path(app.config['UPLOAD_FOLDER']) / filename
            if file_path.suffix != '.csv':
                flash('Invalid file type')
                return redirect(request.url)
            file.save(file_path)
        table = request.form['table']
        db_operations.insert_csv_table(db, file_path, table)
        return redirect('localhost:5000')


app.run(port=5000, host='0.0.0.0', debug=True)