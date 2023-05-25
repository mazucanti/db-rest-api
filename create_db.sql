CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    department TEXT
);

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    job TEXT
);

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    datetime TIMESTAMP,
    department_id INTEGER,
    job_id INTEGER,
    CONSTRAINT fk_department_id
        FOREIGN KEY(department_id)
            REFERENCES departments(id)
            ON DELETE CASCADE,
    CONSTRAINT fk_job_id
        FOREIGN KEY(job_id)
            REFERENCES jobs(id)
            ON DELETE CASCADE
);